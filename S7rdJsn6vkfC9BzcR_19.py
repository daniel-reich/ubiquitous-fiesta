
class Employee:
    def __init__(self, name, salary=None, height=None, nationality=None, subordinates=None):
        self.name, self.lastname = name.split()
        self.salary = salary
        self.height = height
        self.nationality = nationality
        self.subordinates = subordinates

