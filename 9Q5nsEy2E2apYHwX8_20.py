
class programmer:
  def __init__(self, sal, hours):
    # Can't not spell salary properly..
    self._salary = sal
    self._hours  = hours
    
  @property
  def salary(self): return self._salary
  @property
  def work_hours(self): return self._hours
  
  def __del__(self):
    return 'oof, {_salary}, {_hours}'.format(**vars(self))
    
  # Also programmers..
  def compare(*programmers):
    return min(programmers, key=lambda p: (p._salary, p._hours))

