
def avg_note(students):
  avg = lambda a: round(sum(a)/len(a)) if a else 0
  return [{'name': s['name'], 'avgNote': avg(s['notes'])} for s in students]

