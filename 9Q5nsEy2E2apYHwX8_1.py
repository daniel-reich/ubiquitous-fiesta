
class programmer:
  def __init__ (self, sal, ho):
    self.salary = sal
    self.work_hours = ho
  def __del__ (self):
    return "oof, " + str(self.salary) + ", " + str(self.work_hours)
  def compare (self,other):
    if self.salary > other.salary: return self
    if self.salary > other.salary: return other
    if self.work_hours > other.work_hours: return self
    return other

