
def avg_note(students):
  return [{'name': i['name'], 'avgNote': 0 if len(i['notes']) == 0 else round((sum(i['notes']) / len(i['notes'])))} for i in students]

