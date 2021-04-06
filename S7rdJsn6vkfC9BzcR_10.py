
class Employee:
    def __init__(self, name, salary=0, height=0, nationality="", subordinates=[]):
        self.first, self.lastname = name.split(" ")
        self.salary = salary
        self.height = height
        self.nationality = nationality
        self.subordinates = subordinates

