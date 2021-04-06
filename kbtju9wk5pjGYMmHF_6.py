
class Name:
  def __init__(self,f,l):
    self.fname=f.title()
    self.lname=l.title()
    self.fullname='{} {}'.format(self.fname,self.lname)
    self.initials=f[0].upper()+'.'+l[0].upper()

