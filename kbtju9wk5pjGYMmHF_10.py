
class Name:
  def __init__(self, f, l):
    self.fname = f.title()
    self.lname = l.title()
    self.fullname = self.fname + " " + self.lname
    self.initials = self.fname[0] + "." + self.lname[0]

