"""
The restaurant will have different branches.

Each restaurant branch will have a menu.

The menu will have different menu sections, containing different menu items.

The waiter should be able to create an order for a table and add meals for each seat.

Each meal can have multiple meal items. Each meal item corresponds to a menu item.

The system should be able to retrieve information about tables currently available to seat walk-in customers.

The system should support the reservation of tables.

The receptionist should be able to search for available tables by date/time and reserve a table.

The system should allow customers to cancel their reservation.
"""

from abc import ABC
from enum import Enum


class SeatType(Enum):
  REGULAR, KID, ACCESSIBLE, OTHER = 1, 2, 3, 4


class OrderStatus(Enum):
  RECEIVED, PREPARING, COMPLETED, CANCELED, NONE = 1, 2, 3, 4, 5


class TableStatus(Enum):
  FREE, RESERVED, OCCUPIED, OTHER = 1, 2, 3, 4
  
class Customer():

class Person(ABC):

# from abc import ABC, abstractmethod
class Employee(ABC, Person):
  def __init__(self, id, account, name, email, phone):
    super().__init__(name, email, phone)
    self.__employee_id = id
    self.__date_joined = datetime.date.today()
    self.__account = account


class Receptionist(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def create_reservation(self):
    None

#   def search_customer(self, name):
#     None

class Restaurant():
    def __init__(self, name):
        self.__name = name
        self.__branches = []

    def add_branch(self, branch):
        None

class Branch:
  def __init__(self, name, location, kitchen):
    self.__name = name
    self.__location = location
    self.__kitchen = kitchen

  def add_table_chart(self):
    None

class Table:
  def __init__(self, id, max_capacity, location_identifier, status=TableStatus.FREE):
    self.__table_id = id
    self.__max_capacity = max_capacity
    self.__location_identifier = location_identifier
    self.__status = status
    self.__seats = []

  def is_table_free(self):
    None

  def add_reservation(self):
    None

  def search(self, capacity, start_time):
    # return all tables with the given capacity and availability
    None


class TableSeat:
  def __init__(self):
    self.__table_seat_number = 0
    self.__type = SeatType.REGULAR

  def update_seat_type(self, seat_type):
    None


class Reservation:
  def __init__(self, id, people_count, notes, customer):
    self.__reservation_id = id
    self.__time_of_reservation = datetime.datetime.now()
    self.__people_count = people_count
    self.__status = ReservationStatus.REQUESTED
    self.__notes = notes
    self.__checkin_time = datetime.datetime.now()
    self.__customer = customer
    self.__tables = []
    self.__notifications = []

  def update_people_count(self, count):
    None

class MenuItem:
  def __init__(self, id, title, description, price):
    self.__menu_item_id = id
    self.__title = title
    self.__description = description
    self.__price = price

  def update_price(self,  price):
    None


class MenuSection:
  def __init__(self, id, title, description):
    self.__menu_section_id = id
    self.__title = title
    self.__description = description
    self.__menu_items = []

  def add_menu_item(self, menu_item):
    None


class Menu:
  def __init__(self, id, title, description):
    self.__menu_id = id
    self.__title = title
    self.__description = description
    self.__menu_sections = []

  def add_menu_section(self, menu_section):
    None

  def print(self):
    None