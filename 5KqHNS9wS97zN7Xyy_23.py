
def top_note(student):
  student.update({'top_note': max(student['notes'])})
  del student['notes']
  return student

