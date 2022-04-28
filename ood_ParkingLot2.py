"""
- Inheritance
    child class inherits base class methods and attributes
- Polymorphism
    many forms overriding a method(methods to perform different tasks)
- Encapsulation
    Hide the data (open for expation and close for modification)
- Abstraction
    define interface, hide actual implementation details

Design a parking lot:
requirements:
    - private/public
    - types of car
    - multiple cities ?
    - multiple levels
    - no. of spots
    - monthly user/day to day?
    - no. of entry/exit
    - payment system

V1
- public
- 1 building - multiple levels
- types of vehicle (car, bus, motorcycle)
- types of spots (handicap, eco, compact, large, small)
- no. of spots for each type
- single entry/exit
- handicap - (handicap, compact, large)
- motorcycle - (small, compact)
- bus - (large)
- car - (compact, large)

Req:
- new vehicle comes find a parking spot
- 
"""
from abc import ABC, abstractmethod
from enum import Enum


class VehicleType(Enum):
    CAR, MOTORCYCLE, BUS = 1, 2, 3
class SpotType(Enum):
    small, compact, large = 1, 2, 3

class Vehicle(ABC):
    def __init__(self, license_plate, vehicletype) -> None:
        self.__lincense_plate = license_plate
        self.__type = vehicletype
    
    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass

class MotorCycle(Vehicle):
    def __init__(self, license_plate) -> None:
        super(MotorCycle, self).__init__(license_plate, VehicleType.MOTORCYCLE)
    
    def can_fit_in_spot(self, spot):
        return True
    
class Car(Vehicle):
    def __init__(self, license_plate) -> None:
        super(Car, self).__init__(license_plate, VehicleType.CAR)
        
    def can_fit_in_spot(self, spot):
        return True if (spot.spot_type == SpotType.compact) or (spot.spot_type == SpotType.large) else False

class Bus(Vehicle):
    def __init__(self, license_plate) -> None:
        super(Bus, self).__init__(license_plate, VehicleType.BUS)
    
    def can_fit_in_spot(self, spot):
        return True if (spot.spot_type == SpotType.large) else False

class ParkingLot():
    instance = None
    
    class __OnlyOne():
        def __init__(self, levels):
            self.num_lvl = levels
            self.levels = []
    
    def __init__(self, lvls):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(lvls)
        else:
            ParkingLot.instance.num_lvl = lvls
    
    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    
    def remove_vehicle(self, vehicle):
        pass

    def add_levels(self, level):
        pass

class Levels():
    SPOTS_PER_ROW = 10
    
    def __init__(self, floor, total_spots):
        self.floor = floor
        self.num_spots = total_spots
        self.available_spots = 0
        self.parking_spots = []
    
    def add_spots(self, spot):
        pass
    
    def spot_freed(self):
        self.available_spots += 1

    def park_vehicle(self, vehicle):
        spot = self.__find_available_spot(vehicle)
        if spot is None:
            return None
        else:
            spot.park_vehicle(vehicle)
            return spot

    def __find_available_spot(self, vehicle):
        """Find an available spot where vehicle can fit, or return None"""
        for spot in self.parking_spots:
            if spot.vehicle is None and spot.can_fit_vehicle(vehicle):
                return spot
        # ...

    # def __park_starting_at_spot(self, spot, vehicle):
    #     """Occupy starting at spot.spot_number to vehicle.spot_size."""
    #     # ...
        
class ParkingSpot(object):

    def __init__(self, level, row, spot_number, spot_type, vehicle_size):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.vehicle_size = vehicle_size
        self.vehicle = None

    def is_available(self):
        return True if self.vehicle is None else False

    def can_fit_vehicle(self, vehicle):
        if self.vehicle is not None:
            return False
        return vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle):  # ...
    def remove_vehicle(self):  # ...