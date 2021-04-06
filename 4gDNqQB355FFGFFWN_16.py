
def available_spots(lst, num):
  cnt=0
  for i in range(1,len(lst)):
    if (num%2 and (lst[i-1]%2 or lst[i]%2)) or (not num%2 and (not lst[i-1]%2 or not lst[i]%2)):
      cnt+=1
  return cnt

