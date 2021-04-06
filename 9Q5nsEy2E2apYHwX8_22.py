
class programer:
  def __init__ (self, sallary, work_hours):
    self.sallary = sallary
    self.work_hours = work_hours
    
  def __del__ (self):
    return "oof, {}, {}".format(self.sallary, self.work_hours)
  
  def compare (self, a):
    if self.sallary != a.sallary:
      return self if self.sallary < a.sallary else a
    else:
      return self if self.work_hours < a.work_hours else a

