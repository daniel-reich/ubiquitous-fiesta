
def get_student_top_notes(students):
  return [max(x["notes"]) if len(x["notes"]) > 0 else 0 for x in students]

