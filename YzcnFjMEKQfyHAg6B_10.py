
def simon_says(lst1, lst2):
  cnt = 1
  boole = True
  for x in lst1:
    if cnt == len(lst1):
      break
    elif x == lst2[cnt]:
      cnt += 1
    else:
      boole = False
  return(boole)

