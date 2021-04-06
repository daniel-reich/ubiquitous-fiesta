
def get_notes_distribution(students):
  notes = []
  for s in students:
    notes.extend(s['notes'])
  f = [x for x in notes if x in [1,2,3,4,5]]
  return {x: f.count(x) for x in f}

