
def greater_permutation(expr, nums):
  def f(x):
    if x==int(x):
      return int(x)
    else:
      return round(x,2)
  lst=[]
  lst2=[] 
  card=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
  for i in range(6):
    expr2=expr
    a=nums[card[i][0]]
    b=nums[card[i][1]]
    c=nums[card[i][2]]
    expr2 = expr2.replace('a',str(a))
    expr2 = expr2.replace('b',str(b))
    expr2 = expr2.replace('c',str(c))
    finalStr = expr2 + ' = ' + str(f(eval(expr2)))
    lst.append(eval(expr2))
    lst2.append(finalStr)
  x=0
  for i in range(6):
    if lst[x]<lst[i]:
      x=i
  return (lst2[x])

