
class Name():
  def __init__(self,name,last):
    self.fname=name.capitalize()
    self.lname=last.capitalize()
    self.fullname=self.fname+ " "+ self.lname
    self.initials=self.fname[0]+"."+self.lname[0]

