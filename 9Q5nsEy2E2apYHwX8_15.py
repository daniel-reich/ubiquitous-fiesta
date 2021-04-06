
class programmer:
  def __init__ (self, salary, work_hours):
    self.salary = salary
    self.work_hours = work_hours
    
  def __del__ (self):
    return 'oof, {}, {}'.format(self.salary, self.work_hours)
    
  def compare (self, other):
    return self if self.salary < other.salary else other

