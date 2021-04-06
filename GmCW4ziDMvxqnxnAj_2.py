
def who_passed(students):
  return sorted([student for student,grades in students.items() if list(map(lambda x: eval(x),grades)).count(1) == len(grades)])

