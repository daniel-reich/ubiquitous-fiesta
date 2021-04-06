
def get_student_top_notes(students):
  top_notes = []
  for student in students:
    if len(student["notes"]) > 0:
      top_notes.append(max(student["notes"]))
    else:
      top_notes.append(0)
  return(top_notes)

