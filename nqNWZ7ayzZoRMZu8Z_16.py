
def avg_note(students):
  average = lambda lst: 0 if len(lst) == 0 else int(round(sum(lst)/len(lst)))
  return [{"name": d["name"], "avgNote": average(d["notes"])} for d in students]

