
def top_note(student):
  return_dict = dict()
  
  topNote = 0
  for note in student["notes"]:
    topNote = max(topNote, note)
  
  return_dict["name"] = student["name"]
  return_dict["top_note"] = topNote
  return( return_dict)

