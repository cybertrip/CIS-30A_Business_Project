# Global variable declaration
objectList = []
scheduleCounter = 0


# This is where the schedule class will be stored
# Subsequently, the objects will be created here as well
#   appointment is a subclass of schedule
#   delivery is a subclass of schedule
class schedule:
    def __init__(self, subject, destination, expected, company):
        self.subject = ""
        self.destination = ""
        self.expected = ""
        self.company = ""


# This is a child class of schedule where it focuses on appointments
#   Some new arguments were added pertaining to appointments
class appointment(schedule):
    def __init__(self, subject=None, destination=None, expected=None, company=None, contact=None, hours=None, room=None,
                 agent=None):
        super().__init__(subject, destination, expected, company)
        self.hours = hours
        self.room = room
        self.agent = agent
        self.contact = contact


# This is a child class of schedule where it focuses on delivery
#   Some new arguments are added pertaining to deliveries
class delivery(schedule):
    def __init__(self, subject=None, destination=None, expected=None, company=None, tracking=None, origin=None,
                 departed=None, items=None):
        super().__init__(subject, destination, expected, company)
        self.tracking = tracking
        self.origin = origin
        self.departed = departed
        self.items = items
