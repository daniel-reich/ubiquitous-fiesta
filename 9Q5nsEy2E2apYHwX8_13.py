
class programmer:
  def __init__(self, salary, work_hours):
    self.salary = salary
    self.work_hours = work_hours
  def __del__ (self):
    return "oof, {}, {}".format(self.salary, self.work_hours)
  def compare (self, programer):
    if self.salary > programer.salary:
      return programer
    elif self.salary == programer.salary:
      if self.work_hours > programer.work_hours:
        return programer
      else:
        return self
    else:
      return self

