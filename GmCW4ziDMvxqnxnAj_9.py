
def who_passed(students):
  return sorted(s for s in students if all(eval(g)==1 for g in students[s]))

