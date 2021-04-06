
def mark_maths(lst):
  a = [eval(i.replace("=","==")) for i in lst]
  return str(round(sum(a)*100/len(a))) + "%"

