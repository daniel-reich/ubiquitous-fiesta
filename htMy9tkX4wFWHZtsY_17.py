
def palindrome_time(lst):
  c=0
  if lst[0:3]==lst[3:6]:
    return 1
  c=(lst[3]-lst[0])*6
  if lst[4]>lst[1]:
    for i in range(lst[1],lst[4]+1):
      if i%11==0 or i==0:
        c=c+1
  elif lst[4]<lst[1]:
    for i in range(lst[4],lst[1]+1):
      if i%11==0 or i==0:
        c=c-1
  elif lst[4]==lst[1]:
    c=c+1
  if lst[3]<=19 and lst[0]>=16:
    return 0
  elif lst[3]>19 and lst[0]<6:
    c=c-48
    if c<0:
      return 0
    else:
      return c
  elif lst[3]<=9 and lst[0]>=6:
    return 0
  elif lst[3]<16 and lst[3]>9 and lst[0]<6:
    c=c-24
    if c<0:
      return 0
    else:
      return c
  elif lst[0]<5 and lst[3]>19:
    c=c-48
    if c<0:
      return 0
    else:
      return c
  elif lst[3]<5 or lst[0]>9 and lst[3]<16 or lst[0]>19 and lst[3]<=23:
    return c

