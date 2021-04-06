
def score(lst):
  lst2 = list(map(lambda x: eval(x),lst))
  score = lst2.count(1)
  return score == len(lst2)
  
​
def who_passed(students):
  passed = []
  for student in students.keys():
    if score(students[student]) == True:
      passed.append(student)
  return sorted(passed)

