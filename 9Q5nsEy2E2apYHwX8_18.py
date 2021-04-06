
class programer:
  def __init__ (self,sallary,work_hours):
    self.sallary = sallary
    self.work_hours = work_hours
  def __del__ (self):
    return "oof, " + str(self.sallary) + ", " + str(self.work_hours)
  def compare (self,b):
    if(self.sallary<b.sallary):
      return self
    if(self.sallary==b.sallary):
      if(self.work_hours>b.work_hours):
        return self
    return b
    #code

