
class Name:
  def __init__(self, fname, lname):
    self.fname = fname.capitalize()
    self.lname = lname.capitalize()
    self.fullname = "{} {}".format(fname.capitalize(), lname.lower().capitalize())
    self.initials = "{}.{}".format(fname[0], lname[0]).upper()

