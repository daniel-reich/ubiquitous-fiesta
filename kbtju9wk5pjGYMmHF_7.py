
class Name:
    def __init__(self,fname,lname):
        self.fname = fname[0].upper() + fname[1:].lower()
        self.lname = lname[0].upper() + lname[1:].lower()
        self.fullname = fname[0].upper() + fname[1:].lower() + " " + lname[0].upper() + lname[1:].lower()
        self.initials = fname[0].upper() + "." + lname[0].upper()

