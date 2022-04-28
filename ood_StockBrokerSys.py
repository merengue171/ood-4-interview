"""
We have three main Actors in our system:

Admin: Mainly responsible for administrative functions like blocking or unblocking members.
Member: All members can search the stock inventory, as well as buy and sell stocks. Members can have multiple watchlists containing multiple stock quotes.
System: Mainly responsible for sending notifications for stock orders and periodically fetching stock quotes from the stock exchange.
Here are the top use cases of the Stock Brokerage System:

Register new account/Cancel membership: To add a new member or cancel the membership of an existing member.
Add/Remove/Edit watchlist: To add, remove or modify a watchlist.
Search stock inventory: To search for stocks by their symbols.
Place order: To place a buy or sell order on the stock exchange.
Cancel order: Cancel an already placed order.
Deposit/Withdraw money: Members can deposit or withdraw money via check, wire or electronic bank transfer.
"""

from abc import ABC
import datetime
from enum import Enum


class ReturnStatus(Enum):
  SUCCESS, FAIL, INSUFFICIENT_FUNDS, INSUFFICIENT_QUANTITY, NO_STOCK_POSITION = 1, 2, 3, 4, 5, 6


class OrderStatus(Enum):
  OPEN, FILLED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4


class TimeEnforcementType(Enum):
  GOOD_TILL_CANCELLED, FILL_OR_KILL, IMMEDIATE_OR_CANCEL, ON_THE_OPEN, ON_THE_CLOSE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 5


class Location:
  def __init__(self, street, city, state, zip_code, country):
    self._street_address = street
    self._city = city
    self._state = state
    self._zip_code = zip_code
    self._country = country


class Constants:
  def __init__(self):
    self.__MONEY_TRANSFER_LIMIT = 100000
    
class Order(ABC):
  def __init__(self, id):
    self.__order_id = id
    self.__is_buy_order = False
    self.__status = OrderStatus.OPEN
    self.__time_enforcement = TimeEnforcementType.ON_THE_OPEN
    self.__creation_time = datetime.datetime.now()

    self.__parts = {}

  def set_status(self, status):
    self.status = status

  # save in the database
  def save_in_DB(self):
      pass

  def add_order_parts(self, parts):
    for part in parts:
      self.parts[part.get_id()] = part

class LimitOrder(Order):
  def __init__(self):
    self._price_limit = 0.0
    
class Stock():
    def __init__(self, symbol, price) -> None:
        self._symbol = symbol
        self._price = price
    
    def getSymbol(self, symbol):
        return self._symbol
    
    def getPrice(self):
        return self._price
    
    def setPrice(self, price):
        self._price = price

class StockInventory():
    def __init__(self, stock_list_price) -> None:
        self.last_update_time = datetime.datetime.now()
        self.stock_list = {}
        for stock in stock_list_price:
            self.stock_list[stock.getSymbol()] = stock_list_price[stock]
    
    def update(self, ):
        self.last_update_time = datetime.datetime.now()
        #update
    
    def searchSymbol(self, symbol):
        pass

class StockExchange:
  # singleton, used for restricting to create only one instance
  instance = None

  class __OnlyOne:
    def __init__(self):
      None

  def __init__(self):
    if not StockExchange.instance:
      StockExchange.instance = StockExchange.__OnlyOne()

  def placeOrder(self, order):
    return_status = self.get_instance().submit_order(Order)
    return return_status


class Account(ABC):
  def __init__(self, id, password, name, address, email, phone, status=AccountStatus.NONE):
    self._id = id
    self._password = password
    self._name = name
    self._address = address
    self._email = email
    self._phone = phone
    self._status = AccountStatus.NONE

  def reset_password(self):
    None
    
class Admin(Account):
    pass
    
class Member(Account):
  def __init__(self):
    self._available_funds_for_trading = 0.0
    self._date_of_membership = datetime.date.today()
    self._stock_positions = {}
    self._active_orders = {}

  def place_sell_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
    # check if member has this stock position
    if stock_id not in self._stock_positions:
      return ReturnStatus.NO_STOCK_POSITION

    stock_position = self._stock_positions[stock_id]
    # check if the member has enough quantity available to sell
    if stock_position.get_quantity() < quantity:
      return ReturnStatus.INSUFFICIENT_QUANTITY

    order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
    order.is_buy_order = False
    order.save_in_DB()
    success = StockExchange.place_order(order)
    if success:
      order.set_status(OrderStatus.FAILED)
      order.save_in_DB()
    else:
      self.active_orders.add(order.get_order_id(), order)
    return success

  def place_buy_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
    # check if the member has enough funds to buy this stock
    if self._available_funds_for_trading < quantity * limit_price:
      return ReturnStatus.INSUFFICIENT_FUNDS

    order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
    order.is_buy_order = True
    order.save_in_DB()
    success = StockExchange.place_order(order)
    if not success:
      order.set_status(OrderStatus.FAILED)
      order.save_in_DB()
    else:
      self.active_orders.add(order.get_order_id(), order)
    return success

  # this function will be invoked whenever there is an update from
  # stock exchange against an order
  def callback_stock_exchange(self, order_id, order_parts, status):
    order = self.active_orders[order_id]
    order.add_order_parts(order_parts)
    order.set_status(status)
    order.update_in_DB()

    if status == OrderStatus.FILLED or status == OrderStatus.CANCELLEd:
      self.active_orders.remove(order_id)