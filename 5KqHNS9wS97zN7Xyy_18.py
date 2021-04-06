
def top_note(student):
  vals = student['notes']
  maxvals = max(vals)
  student.pop('notes')
  student['top_note'] = maxvals
  return student
print(top_note({ "name": "John", "notes": [3, 5, 4] }))

