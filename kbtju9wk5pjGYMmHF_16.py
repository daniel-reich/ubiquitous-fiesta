
class Name:
    def __init__(self, fname, lname):
      self.fname = fname.capitalize()
      self.lname = lname.capitalize()
      self.fullname = fname.capitalize() + " " + lname.capitalize()
      self.initials = fname[0].upper()+"."+lname[0].upper()

