
def who_passed(students):
  return sorted([s for s in students if all(map(lambda x:x==1,[eval(i) for i in students[s]]))])

