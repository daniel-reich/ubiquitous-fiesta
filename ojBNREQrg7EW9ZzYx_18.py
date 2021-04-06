
def count_eatable_chocolates(money, cost):
  m=''
  for x in money:
    if x in '-0123456789':
      m+=x
  c=''
  for x in cost:
    if x in '-0123456789':
      c+=x
  if int(m)>0 and int(c)>0:
    start=int(m)//int(c)
    count=start
    while start>=3:
      count+=1
      start-=2
    return count
  else:
    return "Invalid Input"

