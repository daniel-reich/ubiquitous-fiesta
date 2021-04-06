
class Name:
  def __init__(self,firstname,lastname):
    self.fname=firstname[0].upper()+firstname.lower()[1:]
    self.lname=lastname[0].upper()+lastname.lower()[1:]
    self.fullname=self.fname+" "+self.lname
    self.initials=self.fname[0]+"."+self.lname[0]

