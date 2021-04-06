
def loves_me(n):
  new = ""
  for i in range(n - 1):
    if i % 2 == 0:
      new += "Loves me, "
    else:
      new += "Loves me not, "
  if n % 2 == 0:
    new += "LOVES ME NOT"
  else:
    new += "LOVES ME"
  return(new)

