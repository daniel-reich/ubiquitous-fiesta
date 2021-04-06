
def every_some(test, val, a, b, c, d, e):
  arr = []
  if val == "everybody":
    for x in [a,b,c,d,e]:
      arr.append(eval(str(x) + test))
    return all(arr)
    
    
  elif val == "somebody":
    for x in [a,b,c,d,e]:
      arr.append(eval(str(x) + test))
    return any(arr)

