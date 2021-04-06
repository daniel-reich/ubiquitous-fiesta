
def how_bad(n):
  print(n)
  p = str(bin(n)).count('1')
  print(p)
  lst=[]
  if p%2 == 0:
    lst.append('Evil')
  elif p%2 == 1:
    lst.append('Odious')
  for i in range(2,p):
    if (p%i) == 0:
      break
    elif (p%i) != 0:
      lst.append('Pernicious')
      break
  if p<=2 and p !=1:
    lst.append('Pernicious')
  return lst

