
def who_passed(students):
  passed = []
  for s in students.items():
    count = 0
    for i in s[1]:
      m = i.split('/')
      if m[0] != m[1]:
        count += 1
    if count == 0:
      passed.append(s[0])
  return sorted(passed)

