
class Name:
    
    def __init__(self, a, b):
        self.fname = a.lower().capitalize()
        self.lname = b.lower().capitalize()
        self.fullname = self.fname + " " + self.lname
        self.initials = self.fname[0] + "." + self.lname[0]

