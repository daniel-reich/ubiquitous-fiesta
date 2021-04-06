
class programer:
  def __init__(self, wage, hours):
    self.sallary = wage
    self.work_hours = hours
  def __del__(self):
    return("oof, " + str(self.sallary) + ", " + str(self.work_hours))
  def compare(self, other):
    return other if self.sallary > other.sallary else self

