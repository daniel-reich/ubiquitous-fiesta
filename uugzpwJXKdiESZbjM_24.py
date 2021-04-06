
def is_full_house(hand):
  lst1=[hand[0]]
  lst2=[]
  for i in range(1,len(hand)):
    if hand[i]==hand[0]:
      lst1.append(hand[i])
    else:
      lst2.append(hand[i])
  l1=len(lst1)
  l2=len(lst2)
  if((l1==3 and l2==2) or (l1==2 and l2==3)):
    return True
  else:
    return False

