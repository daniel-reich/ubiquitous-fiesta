
def avg_note(students):
  avg = []
  for i in students:
    if len(i['notes'])>0:
      temp = round(sum(i['notes'])/len(i['notes']))
    else:
      temp = 0
    avg.append({'name':i['name'],'avgNote':temp})
  return avg

