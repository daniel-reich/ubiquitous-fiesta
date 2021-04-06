
def valid_credit_card(number):
  addup=0
  lst = [int(j) for j in list(str(number))]
  lst.reverse()
  for i in range(len(lst)):
    if i % 2 !=0:
      if lst[i]*2<10:
        addup+=lst[i]*2
      else:
        addup+=sum([int(a) for a in list(str(lst[i]*2))])
    else:
      addup+=lst[i]
  if addup%10==0:
    return True
  else:
    return False

