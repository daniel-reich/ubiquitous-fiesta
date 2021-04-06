
def mult_table(n):
  newlist = []
  multiplier = 1
  for i in range(1,n+1):
    newlist.append(list([x*multiplier for x in range(1,n+1)]))
    multiplier += 1
  return newlist

