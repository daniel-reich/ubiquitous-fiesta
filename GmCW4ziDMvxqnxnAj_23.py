
def who_passed(d):
  num_100s = {}
  passed = []
  for student in d.keys():
    num_100s[student] = 0
  for student in d.keys():
    for test in d[student]:
      if eval(test) == 1:
        num_100s[student] += 1
  for student in num_100s:
    if num_100s[student] == len(d[student]):
      passed.append(student)
  return sorted(passed)

