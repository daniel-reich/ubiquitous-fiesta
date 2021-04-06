
def over_twenty_one(cards):
  list1=[]
  acount = 0
  for elem in cards:
    if elem in ("J","Q","K"):
      list1.append(10)
    elif elem == "A":
      list1.append(11)
      acount +=1
    else:
      list1.append(elem)
  sum=0
  for i in list1:
    sum +=i
  if sum > 21 and acount == 0:
    return True
  elif sum >21:
    sum=sum-10*acount
    return sum>21
  else:
    return False

