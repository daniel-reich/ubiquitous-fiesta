
def top_note(student):
  top = max(student["notes"])
  student.pop("notes")
  student["top_note"] = top
  return student

