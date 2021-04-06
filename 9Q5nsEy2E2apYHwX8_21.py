
class programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours
​
    def __del__(self):
        return 'oof, {}, {}'.format(self.salary, self.work_hours)
​
    def compare(self, other):
        if self.salary < other.salary:
            return self
        elif self.salary > other.salary:
            return other
​
        if self.work_hours < other.work_hours:
            return self
        elif self.work_hours > other.work_hours:
            return other

