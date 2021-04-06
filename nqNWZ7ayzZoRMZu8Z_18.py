
def avg_note(students):
  ans=[]
  for i in students:
    a=round(sum([j for j in i['notes']])/len(i['notes'])) if i['notes'] else 0
    ans.append({'name':i['name'],'avgNote':a})
  return ans

