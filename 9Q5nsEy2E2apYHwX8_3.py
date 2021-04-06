
class programer:
  def __init__ (self, sallary, work_hours):
    self.sallary = sallary
    self.work_hours = work_hours
  def __del__ (self):
    return "oof, " + str(self.sallary) + ", " + str(self.work_hours)
  def compare (self,programer2):
    if self.sallary == programer2.sallary:
      return self if self.work_hours < programer2.work_hours else programer2
    return self if self.sallary < programer2.sallary else programer2

