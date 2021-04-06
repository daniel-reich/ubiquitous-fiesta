
def express_factors(n):
  cat = []
  wrt = get_factors(n)
  cha = sorted(set(wrt),key=wrt.index)
  arr =[[x,wrt.count(x)] for x in cha]
  for i in range(0,len(arr)):
    if arr[i][1]==1:
      cat.append(str(arr[i][0]))
    else:
      cat.append("{}^{}".format(arr[i][0],arr[i][1]))
  return " x ".join(cat)
def get_factors(x):
  lst = []
  for i in range(2, x+1):
    while x%i==0:
      lst.append(i)
      x = x//i
    if x==1:
      break
  return lst

