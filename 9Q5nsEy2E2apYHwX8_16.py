
class programer:
    def __init__ (self, sallary, work_hours):
        self.sallary = sallary
        self.work_hours = work_hours
        
    def __del__ (self):
        msg = 'oof, ' + str(self.sallary) + ', ' + str(self.work_hours)  
        del self
        return msg
        
    def compare (self, other):
        if self.sallary < other.sallary:
            return self
        else:
            return other

