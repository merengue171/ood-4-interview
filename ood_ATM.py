"""
Design an ATM

Customer: The ATM customer can perform the following operations:

Balance inquiry: the user can view his/her account balance.
Cash withdrawal: the user can withdraw a certain amount of cash.
Deposit funds: the user can deposit cash or checks.
Transfer funds: the user can transfer funds to other accounts.


Operator: The operator will be responsible for the following operations:

Turning the ATM ON/OFF using the designated Key-Switch.
Refilling the ATM with cash.
Refilling the ATM’s printer with receipts.
Refilling the ATM’s printer with INK.
Take out deposited cash and checks.

"""
from abc import ABC, abstractmethod
import datetime
from enum import Enum


# class TransactionType(Enum):
#   BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW = 1, 2, 3, 4

class TransactionStatus(Enum):
  SUCCESS, FAILURE, BLOCKED, FULL, PARTIAL, NONE = 1, 2, 3, 4, 5, 6

class Customer():
    def __init__(self, id, name, address, email, phone, account) -> None:
        self.id = id
        self.name = name
        self.address = address
        ...
    
    def makeTransaction(self, id, atm):
        transac_id = id
        transac = Transaction(transac_id, datetime.datetime.now(), TransactionStatus.PARTIAL, self, atm)
        return
    
class Card():
    def __init__(self, number, customer, pin) -> None:
        self.__pin = pin
        ...
    
    def getPin(self):
        return self.__pin
    
class Account(ABC):
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0

    def get_available_balance(self):
        return self.__available_balance
    
class SavingAccount(Account):
    def __init__(self, withdraw_limit):
        self.__withdraw_limit = withdraw_limit


class CheckingAccount(Account):
    def __init__(self, debit_card):
        self.__debit_card = debit_card
    

class ATM():
    def __init__(self, id, location) -> None:
        self.__id = id
        self.__location = location
        self.cash_left = 0
    
    def authenticateUser(self, customer):
        pass

class Transaction(ABC):
  def __init__(self, id, creation_date, status, customer, atm):
    self.__transaction_id = id
    self.__creation_time = creation_date
    self.__status = status
    self.__customer = customer
    self.__atm = atm

  @abstractmethod
  def makeTransation(self):
    None

class BalanceInquiry(Transaction):
  def __init__(self, account_id):
    self.__account_id = account_id

  def get_account_id(self):
    return self.__account_id


class Deposit(Transaction):
  def __init__(self, amount):
    self.__amount = amount

  def get_amount(self):
    return self.__amount


class CheckDeposit(Deposit):
  def __init__(self, check_number, bank_code):
    self.__check_number = check_number
    self.__bank_code = bank_code

  def get_check_number(self):
    return self.__check_number


class CashDeposit(Deposit):
  def __init__(self, cash_deposit_limit):
    self.__cash_deposit_limit = cash_deposit_limit


class Withdraw(Transaction):
  def __init__(self, amount):
    self.__amount = amount

  def get_amount(self):
    return self.__amount
