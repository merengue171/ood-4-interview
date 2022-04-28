"""
https://tedweishiwang.github.io/journal/object-oriented-design-elevator.html
https://leetcode.com/discuss/interview-question/object-oriented-design/1612174/OOD-Elevator

Requirements:
- Users can send requests to the elevator from both outside and inside the elevator.
- The elevator can go up and down in a real-world fashion.
    - When elevator is going up or down, it will stop at all the floors that the users requested.
    - If the elevator received a request of going down while it is going up, the elevator will
      go to the highest floor in the current requests, and then go down.
    - Users can send requests at anytime.
    - The elevator will first process UP requests where request floor is greater than current floor 
      and then process Down requests where request floor is lower than current floor
"""
from enum import Enum
from heapq import heapify, heappop, heappush


class Direction(Enum):
    up = 'UP'
    down = 'DOWN'
    idle = 'IDLE'

class RequestType(Enum):
    external = 'EXTERNAL'
    internal = 'INTERNAL'

class Request:
    def __init__(self, origin, target, typeR, direction):
        self.origin = origin
        self.target = target
        self.typeRequest = typeR
        self.direction = direction

class Button:
    def __init__(self, floor):
        self.floor = floor

class Elevator:
    def __init__(self, currentFloor):
        self.direction = Direction.idle
        self.currentFloor = currentFloor
        self.upStops = []
        self.downStops = []
        # self.capacity = capacity
        # self.num_ppl = headcount
        heapify(self.upStops)
        heapify(self.downStops)

    def takeUpRequest(self, upRequest):
        if upRequest.typeRequest == RequestType.external:
            heappush(self.upStops, (upRequest.origin, upRequest.origin))
        heappush(self.upStops, (upRequest.target, upRequest.origin))

    def takeDownRequest(self, downRequest):
        if downRequest.typeRequest == RequestType.external:
            heappush(self.downStops, (-downRequest.origin, downRequest.origin))
        heappush(self.downStops, (-downRequest.target, downRequest.origin))

    def run(self):
        while self.upStops or self.downStops:
            self.processRequests()

    def processRequests(self):
        if self.direction in [Direction.up, Direction.idle]:
            self.processUpRequests()
            self.processDownRequests()
        else:
            self.processDownRequests()
            self.processUpRequests()

    def processUpRequests(self):
        while self.upStops:
            target, origin = heappop(self.upStops)

            self.currentFloor = target

            if target == origin:
                print("Stopping at floor {} to pick up people".format(target))
            else:
                print("stopping at floor {} to let people out".format(target))

        if self.downStops:
            self.direction = Direction.down
        else:
            self.direction = Direction.idle

    def processDownRequests(self):
        while self.downStops:
            target, origin = heappop(self.downStops)

            self.currentFloor = target

            if abs(target) == origin:
                print("Stopping at floor {} to pick up people".format(abs(target)))
            else:
                print("stopping at floor {} to let people out".format(abs(target)))

        if self.upStops:
            self.direction = Direction.up
        else:
            self.direction = Direction.idle


elevator = Elevator(0)
upRequest1 = Request(elevator.currentFloor, 5, RequestType.internal, Direction.up)
upRequest2 = Request(elevator.currentFloor, 3, RequestType.internal, Direction.up)

downRequest1 = Request(elevator.currentFloor, 1, RequestType.internal, Direction.down)
downRequest2 = Request(elevator.currentFloor, 2, RequestType.internal, Direction.down)

upRequest3 = Request(4, 8, RequestType.external, Direction.up)
downRequest3 = Request(6, 3, RequestType.external, Direction.down)

elevator.takeUpRequest(upRequest1)
elevator.takeUpRequest(upRequest2)

elevator.takeDownRequest(downRequest1)
elevator.takeDownRequest(downRequest2)

elevator.takeUpRequest(upRequest3)
elevator.takeDownRequest(downRequest3)

elevator.run()