
def lower_triang(arr):
  a=0
  ans=[]
  for i in arr:
    b=[]
    for j in range(len(i)):
      if j>a: b.append(0)
      else: b.append(i[j])
    a+=1
    ans.append(b)
  return ans

