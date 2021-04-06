
class Name:
  def __init__(self, fname='', lname=''):
    self.fname = fname.capitalize()
    self.lname = lname.capitalize()
    self.fullname = self.fname + ' ' + self.lname
    self.initials = self.fname[0] + '.' + self.lname[0]

