
class programer:
  def __init__ (self, sallery, work_hours):
      self.sallary = sallery
      self.work_hours = work_hours
    
  def __del__ (self):
    #code
      return "oof, " + str(self.sallary) + ", " + str(self.work_hours)
  
  def compare (self, other_programmer):
    #code
      if self.sallary == other_programmer.sallary:
          if self.work_hours < other_programmer.work_hours:
              return self
          else:
              return other_programmer
      else:
          if self.sallary < other_programmer.sallary:
              return self
          else:
              return other_programmer

