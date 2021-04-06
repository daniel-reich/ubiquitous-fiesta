
def who_passed(students):
  passed = []
  for student in students:
    perfect = True
    for score in students.get(student):
      sepScore = score.split('/')
      if sepScore[0] != sepScore[1]:
        perfect = False
        break
    if perfect == True:
      passed.append(student)
  return sorted(passed)

