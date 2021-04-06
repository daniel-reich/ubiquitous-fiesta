
def how_many_times(msg):
  a=[]
  for i in msg:
    a.append(ord(i))
  sum=0
  for i in a:
    sum+=i
  return sum-(len(msg)*96)

