
class programer():
    def __init__(self,sallary,work_hour):
        self.sallary = sallary
        self.work_hours = work_hour
    def __del__(self):
        return "oof, " + str(self.sallary) + ", " + str(self.work_hours)
    def compare(self,prog2):
        if self.sallary>prog2.sallary:
            return prog2
        else:
            return self

