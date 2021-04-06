
def top_note(student):
  student.update({'top_note': max(student.pop('notes'))})
  return student

