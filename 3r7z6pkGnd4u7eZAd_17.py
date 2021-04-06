
def mark_maths(lst):
  f = [eval(i.split("=")[0]) for i in lst]
  s = [int(i.split("=")[1]) for i in lst]
  return str(round((len([v for i,v in enumerate(f) if v == s[i]])/len(lst))*100))+"%"

