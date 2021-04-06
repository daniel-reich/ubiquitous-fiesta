
def get_student_top_notes(students):
  return[0 if not student['notes'] else max(student['notes']) for student in students]

