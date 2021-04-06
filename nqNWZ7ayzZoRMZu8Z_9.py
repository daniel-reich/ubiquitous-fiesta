
def avg_note(students):
  return [{'name':x['name'],'avgNote':round(sum(x['notes'])/len(x['notes'])) if x['notes'] else 0} for x in students]

