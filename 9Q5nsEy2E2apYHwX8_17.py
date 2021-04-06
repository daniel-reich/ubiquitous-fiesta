
class programer:
    def __init__ (self,sallary,work_hours):
        self.sallary = sallary
        self.work_hours = work_hours
        
    def __del__ (self):
        return "oof, " + str(self.sallary) + ", " + str(self.work_hours)
        
    def compare(self,other):
        the_worst = self
        if other:
            if self.sallary > other.sallary:
                the_worst = other
​
            elif (self.sallary== other.sallary):
                if(self.work_hours > other.work_hours):
                    the_worst = self
        return the_worst

