"""
Design meeting scheduler:

Requirements:
- there are n given meeting rooms.
- Book a meeting in any meeting room at given interval (starting time, end time, capacity).
- Also send notifications to all person who invited for meeting.
- use calendar for tracking date and time.
- also history of all the meeting which are booked an meeting room.

"""

class User:
    def __init__(self, name, email) -> None:
        self.__name = name
        self.__email = email

class Interval():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

class MeetingRoom():
    def __init__(self, capacity, id, location) -> None:
        self.id = id
        self.location = location
        self.capacity = capacity
        self.calendar = Calendar(id)
    
    def isAvailable(self, interval):
        self.calendar.checkAvailable(interval)
    
    def scheduleMeeting(self, interval, users):
        self.calendar.bookInterval(interval)
        return self.calendar.scheduleMeeting(interval, users)

class Calendar():
    
    intervals = []
    meetings = []
    def __init__(self, room_id):
        self.room_id = room_id
    
    def checkAvailable(self, interval):
        for inter in self.intervals:
            if interval.end > inter.start or interval.start < inter.end:
                return False
        return True
    
    def bookInterval(self, interval):
        self.intervals.append(interval)
    
    def scheduleMeeting(self, interval, users):
        meeting = Meeting(interval, self.room_id)
        meeting.notifyUsers(users)
        self.meetings.append(meeting)
        return meeting

class Template():
    def __init__(self, subject, user_email, interval):
        pass

class Notifications():
    def sendEmails(template, users):
        pass
    
class Meeting():
    def __init__(self, interval, room_id) -> None:
        self.room_id = room_id
        self.interval = interval
        self.users = []
        self.notification = Notifications()
    
    def notifyUsers(self):
        # self.users.extend(users)
        self.notification.sendEmail(template, users)

class MeetingScheduler:
    def __init__(self) -> None:
        self.meeting_rooms = [] # another method to generate meeting rooms
    
    def bookMeeting(self, interval, users):
        for room in self.meeting_rooms:
            if room.isAvailable(interval):
                meeting = room.scheduleMeeting(interval, users)
                return meeting
        return None
    
    def cancelMeeting(self, meeting):
        pass