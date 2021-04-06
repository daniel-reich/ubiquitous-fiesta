
def maxmin(n):
  print (n)
  return (swap(n,True), swap(n,False))
​
def swap(n, revers):
  n  = list(str(n))
  # print(n)
  p = sorted(n,reverse= revers)
  print(p)
  i = 0
  while n[i] == p[i]:
    if i == len(n)-1:
      return int("".join(n))
    i += 1
  k = i
  if not revers:
    if i == 0:
      if int(n[i]) == min([int(v) for _,v in enumerate(n) if v != "0"]):
        i +=1
        while n[i] == '0':
          if i == len(n)-1:
            return int("".join(n))
          i += 1
      else:
        while p[k] == "0":
          if k == len(n)-1:
            return int("".join(n))
          k += 1
​
  j = len(n) -i -1 - n[i:][::-1].index(p[k])
  print (i,k,j)
  n[i],n[i+j] = n[i+j], n[i]
  return int("".join(n))

