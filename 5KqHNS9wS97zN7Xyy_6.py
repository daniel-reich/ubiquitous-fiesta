
def top_note(student):
  vals = student["notes"]
  max_vals = max(vals)
  print(max_vals)
  student.pop('notes')
  student['top_note'] = max_vals
  return student
print(top_note({ "name": "John", "notes": [3, 5, 4] }))

