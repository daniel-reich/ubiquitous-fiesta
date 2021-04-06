
def get_notes_distribution(students):
  notes = sum([i['notes'] for i in students], [])
  return {i: notes.count(i) for i in set(notes) if 1 <= i <= 5}

