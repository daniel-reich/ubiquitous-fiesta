
def ABA(s):
  a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  arr = []
  for i in range(a.index(s)+1):
    if len(arr) > 0:
      l = arr[-1]
      arr.append(l + a[i] + l)
    else : arr.append(a[i])
  return arr[-1]

