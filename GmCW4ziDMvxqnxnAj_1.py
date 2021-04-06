
def who_passed(students):
  return sorted(name for name, grades in students.items() if all(eval(i) == 1 for i in grades))

