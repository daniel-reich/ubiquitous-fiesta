
def top_note(student):
  student["top_note"] = max(student["notes"])
  student.pop("notes")
  return student

