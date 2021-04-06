
def mark_maths(lst):
  return str(round(sum([1 for x in lst if eval(x.split("=")[0]) == int(x.split("=")[1]) ])/len(lst) * 100))+"%"

