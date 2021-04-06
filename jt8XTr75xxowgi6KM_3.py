
def get_student_top_notes(students):
  return [max(s["notes"]) if s["notes"] else 0 for s in students]

