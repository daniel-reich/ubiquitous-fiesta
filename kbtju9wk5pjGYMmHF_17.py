
class Name:
  def __init__(self, first_name, last_name):
    self.fname = first_name.capitalize()
    self.lname = last_name.capitalize()
    self.fullname = self.fname + ' ' + self.lname
    self.initials = self.fname[0]+'.'+self.lname[0]

