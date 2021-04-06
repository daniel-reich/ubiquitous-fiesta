
class Employee:
  def __init__(self, name, salary=0, height=0, nationality="",subordinates=[]):
    self.divide = name
    self.name = self.first()[0]
    self.lastname = self.first()[1]
    self.salary = salary
    self.height = height
    self.nationality = nationality
    self.subordinates = subordinates
    
  def first(self):
    return[self.divide[:self.divide.index(" ")], self.divide[self.divide.index(" ") + 1:]]

