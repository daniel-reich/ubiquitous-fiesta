
class Employee:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.fullname =  self.firstname + ' ' + self.lastname
    self.email=  (self.firstname).lower() + '.' + (self.lastname).lower() + '@company.com'

