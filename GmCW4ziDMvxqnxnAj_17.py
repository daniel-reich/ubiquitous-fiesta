
def who_passed(students):
  passed = []
  for student, marks in students.items():
    for mark in marks:
      if eval(mark) != 1: break
    else:
      passed.append(student)
      
  return sorted(passed)

