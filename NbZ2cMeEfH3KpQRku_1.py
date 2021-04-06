
def portion_happy(n):
  count = 0
  for i in range(1,len(n)-1):
    if n[i] == n[i-1] or n[i] == n[i+1]:
      count+=1
  if n[0] == n[1]:
    count+=1
  if n[-1] == n[-2]:
    count+=1
  return count/len(n)

