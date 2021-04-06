
class Employee:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    # Complete the code!
    self.fullname = self.firstname + " " + self.lastname
    self.email = (self.firstname + "." + self.lastname + "@company.com").lower()

