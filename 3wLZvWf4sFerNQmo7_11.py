
def neutralise(lst1, lst2):
  a1 = list(lst1)
  b2 = list(lst2)
  c = []
  for i in range(len(a1)):
    c.append(a1[i]+b2[i])
​
  result=[]
​
  for i in c:
    if i == '++':
      result.append('+')
    elif i == '--':
      result.append('-')
    elif i == '+-' or i == '-+':
      result.append('0')
​
  return ''.join(result)

