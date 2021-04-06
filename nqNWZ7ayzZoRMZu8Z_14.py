
def avg_note(students):
  res=[{} for _ in range(len(students))]
  for i in range(len(res)):
    res[i]['name']=students[i]['name']
    res[i]['avgNote']=round(sum(students[i]['notes'])/len(students[i]['notes'])) if students[i]['notes'] else 0
  return res

