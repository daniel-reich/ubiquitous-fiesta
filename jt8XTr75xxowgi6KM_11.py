
def get_student_top_notes(students):
  return list(map(lambda x: max(x["notes"] if x["notes"] else [0]), students))

