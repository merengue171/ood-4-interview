"""
Design is always defined into Higher abstraction => abstraction => structure of classes => 
class member and behavior required to handle the requirement but no definition of interface => 
Few Use case flow diagram using some sequence and after this if interviewer need more clarity 
on some class and member and their behavior in detail then explain implementation approach. 
But major part focus should be on structure of class and how these classes together interacting and 
accomplishing the overall system to meet the end goal.

Implement Vending Machine:

- Add items to the vending machine in fixed number of slots
- Select item to dispense
- What type of items in Vending machines
- Payment using card or cash
"""
from enum import Enum


class Items(Enum):
    coldDrinks, snacks, salads = 1,2,3
class paymentType(Enum):
    CASH, CARD = 1, 2

class Product():
    def __init__(self, pid, typeItem, price) -> None:
        self.pid = pid
        self.type = typeItem
        self.price = price
    
    def getPrice(self):
        return self.price

class VendingMachine():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.slots = {}
        self.product_list = []
        
    def addProduct(self, prod):
        if len(self.slots) >= self.capacity:
            return False
        self.slots[prod.pid] = prod
        return True
    
    def orderProducts(self, prod):
        self.product_list.append(self.slots[prod.pid])
    
    def checkout(self, payType):
        payment = PaymentSystem()
        total_price = 0
        for item in self.product_list:
            total_price += item.getPrice()
        if payment.makePayment(total_price, payType):
            return True
    
    def dispense(self):
        for item in self.product_list:
            del self.slots[item.pid]
        return self.product_list

class PaymentSystem():
    def __init__(self):
        pass
    
    def makePayment(self, total_price, payType):
        if payType == paymentType.CARD:
            __payCard(total_price)
        else:
            __payCash(total_price)
        return True

class Customer():
    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine
        self.__paid_successfully = False
        
    def pay_for_products(self, payment_type):
        if self.vending_machine.checkout(payment_type):
            self.__paid_successfully = True
    
    def makeSelection(self, product_item):
        item = self.vending_machine.orderProducts(product_item)
    
    def dispenseOrder(self):
        if self.__paid_successfully == True:
            return self.vending_machine.dispense()
        else:
            raise ValueError('not paid yet')

# Main():
VM = VendingMachine()
cust = Customer(VM)
cust.makeSelection(items)
cust.pay_for_products()
cust.dispenseOrder()


# class Supplier():
#     def __init__(self) -> None:
#         pass