
def who_passed(students):
  return sorted([student for student, grades in students.items() if all(eval(grade)==1 for grade in grades)])

