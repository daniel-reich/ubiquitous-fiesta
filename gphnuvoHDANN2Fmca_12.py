
def odd_sort(lst):
​
  t=[]
  result=["_"]*len(lst)
  for i in range(len(lst)):
    if lst[i]%2==0:
      result[i]=lst[i]
    else:
      t.append(lst[i])
  
  t=sorted(t)
  j=0
  for i in range(len(result)):
    if result[i]=="_":
      result[i]=t[j]
      j=j+1
  return result

