
class Name:
  def __init__(self,fname, lname):
    self.fname = fname.title()
    self.lname = lname.title()
    self.fullname = fname.title() + ' ' + lname.title()
    self.initials = fname.title()[0] + '.' + lname.title()[0]

