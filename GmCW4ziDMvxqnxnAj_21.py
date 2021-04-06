
def who_passed(students):
  result = []
  for k in students:
    t = True
    for i in students[k]:
      x = i.split("/")
      if x[0] != x[1]:
        t = False
    if t:
      result.append(k)
  return sorted(result)

