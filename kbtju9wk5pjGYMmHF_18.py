
class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = fname.capitalize() + ' ' + lname.capitalize()
        self.initials = fname.capitalize()[0] + '.' + lname.capitalize()[0]

