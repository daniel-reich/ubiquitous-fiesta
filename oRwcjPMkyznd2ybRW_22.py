
def max_product(n):
 great=0
 lst=[0]
 for i in range(0,n+1):
  result=1
  for b in str(i):
   result=result*int(b)
  if result==great:
   lst.append(i)
  if result>great:
   lst.clear()
   lst.append(i)
   great=result
​
 return lst

