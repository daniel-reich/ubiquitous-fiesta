
def get_notes_distribution(students):
    notes = sum([student['notes'] for student in students], [])
    return {i:notes.count(i) for i in range(1, 6) if notes.count(i) !=0}

