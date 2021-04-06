
def get_student_top_notes(students):
  return [max(i['notes']) if i['notes'] else 0 for i in students]

