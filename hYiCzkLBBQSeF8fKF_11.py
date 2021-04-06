
def count(d):
  add = 0
  for i in d:
    if i in range(2, 7): add = add+1
    elif i in range (7, 10): add = add+0
    else: add = add-1
  return(add)

