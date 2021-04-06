
def get_notes_distribution(students):
  valid = {1, 2, 3, 4, 5}
  distribution = {}
  for student in students:
    for note in student['notes']:
      if note in valid:
        if note in distribution:
          distribution[note] += 1
        else:
          distribution[note] = 1
  return distribution

