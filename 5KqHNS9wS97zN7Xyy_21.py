
def top_note(student):
  dct = {}
  dct["name"] = student.get("name")
  dct["top_note"] = max(student.get("notes"))
  return dct

