
def get_notes_distribution(students):
  res = {}
  for student in students:
    for note in [n for n in student['notes'] if 1<=n<=5]:
      res[note] = res[note] + 1 if note in res else 1
  return res

