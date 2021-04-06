
def integer_boolean(n):
  lst = []
  for i in n:
    if int(i) == 1:
      lst.append(True)
    else:
      lst.append(False)
  return lst

