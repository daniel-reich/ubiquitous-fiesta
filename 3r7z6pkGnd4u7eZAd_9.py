
def mark_maths(lst):
  new_list = []
  for i in lst:
    x = i.replace("=", "==")
    if eval(x):
      new_list.append(1)
  perc = len(new_list) / len(lst)
  return str(round(perc * 100)) + "%"

