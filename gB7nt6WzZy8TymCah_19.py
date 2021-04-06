
class Employee:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.fullname = "%s %s" % (self.firstname, self.lastname)
    self.email    = ("%s.%s@company.com" % (self.firstname, self.lastname)).lower()
    # Complete the code!

