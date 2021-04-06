
class Name:
​
  def __init__(self, f, l):
    f = f.title()
    l = l.title()
    self.fname = f
    self.lname = l
    self.fullname = f + ' ' + l
    self.initials = f[0] + '.' + l[0]

