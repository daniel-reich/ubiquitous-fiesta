
def get_notes_distribution(students):
  notes = {}
  for student in students:
    for value in student['notes']:
      if value in list(range(1,6)):
        try:notes[value] += 1   
        except KeyError: notes[value] = 1
  for note in notes:
    if notes[note] == 0:
      del notes[note]
  return notes

