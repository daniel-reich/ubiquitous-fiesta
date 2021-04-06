
def get_student_top_notes(students):
  
  top_notes = []
  
  for student in students:
    try:
      top_notes.append(max(student['notes']))
    except ValueError:
      top_notes.append(0)
  
  return top_notes

