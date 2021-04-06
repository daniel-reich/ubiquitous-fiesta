
def avg_note(students):
  res = []
  for s in students:
    avg = round(sum(s["notes"]) / len(s["notes"])) if s["notes"] else 0
    res.append({"name": s["name"], "avgNote": avg})
  return res

