
def mark_maths(lst):
  correct_count = 0
  for x in lst:
    if eval(x.split("=")[0]) == int(x.split("=")[1]):
      correct_count += 1
  return str(round(correct_count/len(lst)*100)) + "%"

