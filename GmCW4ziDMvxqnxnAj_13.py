
def who_passed(students):
  perf = []
  l = []
  for student, grade in students.items():
    for mark in grade:
      mark = mark.split("/")
      if mark[0] != mark[1]:
        break
      perf.append(student)
    if perf.count(student) == len(grade):
      l.append(student)
  return sorted(l)

