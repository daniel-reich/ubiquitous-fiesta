
def currently_winning(scores):
  a,b,ans = [],[],[]
  for x in range(len(scores)):
    if x % 2 == 0:
      a.append(scores[x])
    else:
      b.append(scores[x])
  y = [a[0]]
  o = [b[0]]
  sum = a[0]
  for x in range(1,len(a)):
    sum += a[x]
    y.append(sum)
  sum = b[0]
  for x in range(1,len(a)):
    sum += b[x]
    o.append(sum)
  for x in range(len(y)):
    if y[x] > o[x]:
      ans.append("Y")
    elif o[x] > y[x]:
      ans.append("O")
    else:
      ans.append("T")
  return ans

