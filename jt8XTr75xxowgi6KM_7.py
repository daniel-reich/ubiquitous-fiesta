
def get_student_top_notes(students):
  lst=[max(l["notes"]) if len(l["notes"])>0 else 0 for l in students]
  return lst

