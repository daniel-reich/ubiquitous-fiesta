
class programer:
  def __init__ (self, sallary, work_hours):
    self.sallary = sallary
    self.work_hours = work_hours
  def __del__ (self):
    return 'oof, {}, {}'.format(self.sallary, self.work_hours)
  def compare (self, prog):
    if self.sallary > prog.sallary: return prog
    elif self.sallary < prog.sallary: return self
    else:
      if self.work_hours > prog.work_hours: return prog
      else: return self

