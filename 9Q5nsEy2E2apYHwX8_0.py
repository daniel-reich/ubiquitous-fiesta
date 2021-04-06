
class programmer:
  def __init__ (self,s,w):
    self.salary= s
    self.work_hours=w
  def __del__ (self):
    return "oof, {}, {}".format(self.salary, self.work_hours)
  def compare (self,other):
    return sorted([self,other], key=lambda x:x.salary)[0]

