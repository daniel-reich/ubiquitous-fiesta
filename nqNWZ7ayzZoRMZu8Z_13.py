
def avg_note(stud):
  for x in stud:
    if x['notes']:
      x.update({'avgNote': round(sum(x['notes']) / len(x['notes']))})
    else: x.update({'avgNote': 0})
  [x.pop('notes') for x in stud]
  return stud

