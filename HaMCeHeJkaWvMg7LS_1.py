
def sun_loungers(beach):
  ones = []
  for i in range(len(beach)):
    if beach[i] == '1':
      ones.append(i)
  
  if not ones:
    return (len(beach)+1)//2
  
  ans = sum((b-a-2)//2 for a,b in zip(ones, ones[1:]))
  ans += ones[0]//2
  ans += (len(beach) - ones[-1]-1)//2
  
  return ans

