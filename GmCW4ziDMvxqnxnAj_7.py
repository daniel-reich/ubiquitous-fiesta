
def who_passed(students):
  pas = [k for k in students.keys()]
  for k,v in students.items():
    if any(eval(exam) != 1 for exam in v): pas.remove(k)
  return sorted(pas)

