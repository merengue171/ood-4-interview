"""
to monitor the process of how to put the package into a right locker. and one locker for one package. your package and locker have different size, you need to make sure  locker size > package.

Requiements:

- Delivery guy should be able to find an "optimal" locker for a package.
- System should send code to the user.
- Users should be able to use a code to open a locker and pick up a package/packages.

- Assign location based on user location.
- Assume there is always a locker available.
"""
from enum import Enum

class Size(Enum):
	Small, Medium, Large = 1, 2, 3
 
class Status(Enum):
    Deliver, Transit, Not_picked, Picked = 1, 2, 4, 5

class Locker():
	def __init__(self, size, id):
		self.size = size
		self.id = id
		self.isAvailable = True
		self.package = None
	
	def getSize(self):
		return self.size
	
	def isAvailable(self):
		return self.isAvailable
	
	def addPackage(self, package):
		self.isAvailable = False
		self.package = package
	
	def removePackage(self):
		self.isAvailable = True
	
class Package():
	def __init__(self, id, packageSize, user):
		self.id = id
		self.size = packageSize
		self.user = user
		self.status = None
  
	def notifyUser(self):
		pass

class Code():
    def __init__(self):
        self.code = None
        self.expire = False
        
class User():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def pickUp(self, code, LockerSys):
        return LockerSys.pickUp(code)
        

class DeliveryPerson():
	def __init__(self, lockerService, packages):
		self.packages = packages
  
	def executeDelivery(self):
		for package in self.packages:
			package.status = Status.Not_picked
			lockerSys = self.lockerService.getLockerSys(package)
			lockerSys.addPackage(package)

class LockerSystem:
	def __init__(self, id, locationId):
		self.id = id
		self.location = locationId
		self.smallLockers = [] #generate list of small lockers
		self.largeLockers = [] #
		self.mediumLockers = []
		self.assignLockerMap = {}
		# self.lockerMap = {}
	
	def __generateCode():
		pass

	def __findLocker(self, package):
		if package.size == Size.small:
			for locker in self.smallLockers:
				if locker.isAvailable:
					locker.isAvailable = False
					return locker
		if package.size == Size.medium:
			for locker in self.mediumLockers:
				if locker.isAvailable:
					locker.isAvailable = False
					return locker
		if package.size == Size.large:
			for locker in self.largeLockers:
				if locker.isAvailable:
					locker.isAvailable = False
					return locker
		return None

	def pickUp(self, lockerCode):
		# find locker
		# open locker
		# if code expire then return error
		if lockerCode not in self.assignLockerMap:
			return "Exception"

		code = self.assignLockerMap[lockerCode][0]
		if not code.expire:
			locker = self.assignLockerMap[lockerCode][1]
			package = locker.removePackage()
			del self.assignLockerMap[lockerCode]
			return package

	def addPackage(self, package):
		# finding the locker
		# generate the code and add to the locker
		# notify user
		# full return back to del
		locker = self.__findLocker(package)
		if not locker:
			return "Return package"
		locker.addPackage(package)
		codeObject = self.__generateCode()
  
		self.assignLockerMap[codeObject.code] = [codeObject.code, locker]
		user = package.user
		package.notifyUser(user)
		return











