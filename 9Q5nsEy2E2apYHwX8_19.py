
class programer:
    def __init__ (self, sallary, work_hours):
        self.sallary = sallary
        self.work_hours = work_hours
        
    def __del__ (self):
        return "oof, " + str(self.sallary) + ", " + str(self.work_hours)
        
    def compare(self, other):
        if self.sallary > other.sallary:
            return other
        elif self.sallary == other.sallary and self.work_hours > other.work_hours:
            return other
        else:
            return self

