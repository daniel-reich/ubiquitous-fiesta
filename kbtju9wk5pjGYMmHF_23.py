
class Name:
  def __init__(self, fname, lname):
    self.fname = fname.capitalize()
    self.lname = lname.capitalize()
  @property
  def fullname(self):
    return "{} {}".format(self.fname, self.lname)
  @property
  def initials(self):
    return "{}.{}".format(self.fname[0], self.lname[0])

