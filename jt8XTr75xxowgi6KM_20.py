
def get_student_top_notes(students):
  return [max(x['notes']) if x['notes'] else 0 for x in students]

