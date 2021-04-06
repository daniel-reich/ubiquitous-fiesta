
def war_of_numbers(lst):
  even = []
  odd = []
  
  for x in range(len(lst)):
    if lst[x] % 2 == 0:
      even.append(lst[x])
    else:
      odd.append(lst[x])
  sum1,sum2 = sum(even),sum(odd)
  
  if sum1>sum2:
    return sum1-sum2
  elif sum1<sum2:
    return sum2-sum1
  else:
    return 0

