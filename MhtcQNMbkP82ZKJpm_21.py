
def get_notes_distribution(students):
  def valid_notes_list_creator(students):
    valid_notes = []
    valid = [1, 2, 3, 4, 5]
    for student in students:
      notes = student['notes']
      for note in notes:
        if note in valid:
          valid_notes.append(note)
    return valid_notes
  
  valid_notes = valid_notes_list_creator(students)
  note_dic = {}
  
  for note in valid_notes:
    if note not in note_dic.keys():
      note_dic[note] = valid_notes.count(note)
  
  return note_dic

