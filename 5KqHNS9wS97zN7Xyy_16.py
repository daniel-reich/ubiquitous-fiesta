
def top_note(student):
  newDict = {}
  newDict['name'] = student.get('name')
  newDict['top_note'] = max(student.get('notes'))
  return newDict

