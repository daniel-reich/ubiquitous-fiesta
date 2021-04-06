
def who_passed(students):
  
  class Student:
  
    def __init__(self, name, grades):
      self.n = name
      self.g = grades
    
    def passed(self):
      
      grades = []
      print('hi')
      for grade in self.g:
        grades.append(eval(grade))
      print(grades)
      return grades.count(1) == len(grades)
  
  studnts = []
  
  for student in students.keys():
    s = Student(student, students[student])
    studnts.append(s)
  
  pssed = []
  
  for student in studnts:
    if student.passed() == True:
      pssed.append(student.n)
  
  return sorted(pssed)

