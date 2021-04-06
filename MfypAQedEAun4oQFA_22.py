
def perrin(n):
  list1=[3,0,2]
  sum1=3
  while sum1!=(n+1):
    a=list1[-2]+list1[-3]
    list1.append(a)
    sum1+=1
  return list1[-1]

