
def integer_boolean(n):
  lst = []
  for i in n:
    if str(i) == "0":
      lst.append(False)
      continue
    elif str(i) == "1":
      lst.append(True)
  
  return lst

