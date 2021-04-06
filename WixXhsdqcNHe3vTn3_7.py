
def how_bad(n):
  flag = True
  lst = []
  number = bin(n).count("1")
  
  for foo in range(2, number // 2 + 1):
    if number % foo == 0:
      flag = False
      break
  if number % 2 == 0:
    lst.append("Evil")
  else:
    lst.append("Odious")
  if flag and number >= 2:
    lst.append("Pernicious")
  return lst

