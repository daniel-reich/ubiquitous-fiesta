
import math
def pascals_triangle(n):
  ans=[]
  row=1
  for i in range(n):
    for k in range(row):
      ans.append(math.factorial(i)/(math.factorial(k)*math.factorial(i-k)))
    row+=1
  return ans

