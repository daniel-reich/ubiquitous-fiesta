
def top_note(student):
  vals = student['notes']
  max_val = max(vals)
  student.pop('notes')
  student['top_note'] = max_val
  return student
​
​
print(top_note({ "name": "John", "notes": [3, 5, 4] }))

