
def get_student_top_notes(students):
  return [max(d["notes"]) if d["notes"] else 0 for d in students]

