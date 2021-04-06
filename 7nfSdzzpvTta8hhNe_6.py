
def organize(txt):
  if txt=="":
    return {}
  d={}
  for x,y in zip(["name","age","occupation"],txt.split(", ")):
    if y.isdigit(): 
      d[x]=int(y)
    else:
      d[x]=y
  return d

