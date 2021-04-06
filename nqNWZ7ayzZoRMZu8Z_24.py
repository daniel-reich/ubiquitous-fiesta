
def avg_note(students):
  return [{"name":i["name"],"avgNote":round(sum(i["notes"])/len(i["notes"])) if i["notes"] else 0} for i in students]

