
def available_spots(lst, num):  
  count = 0
  for x in range(1,len(lst)):
    if num%2:
      if (lst[x])%2 or (lst[x-1])%2:
        count+=1
    else:
      if (lst[x])%2==0 or (lst[x-1])%2==0:
        count+=1
  return count

