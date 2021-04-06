
def last_name_lensort(names):
  names = sorted(names, key=alp)
  names = sorted(names, key=numeric)
  return names
​
def alp(w):
  w = w.split(" ")
  return w[1][0]
  
def numeric(w):
  w = w.split(" ")
  return len(w[1])

