
def avg_note(students):
  l=[]
  for x in students:
    d={"name":x["name"]}
    if not x["notes"]:
      d["avgNote"]=0
    else:
      d["avgNote"]=round(sum(x["notes"])/len(x["notes"]),0)
    l.append(d)
  return l

