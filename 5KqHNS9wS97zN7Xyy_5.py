
def top_note(student):
  notes_list = student["notes"]
  name = student["name"]
  top_note = max(notes_list)
  
  return {"name":name, "top_note":top_note}

