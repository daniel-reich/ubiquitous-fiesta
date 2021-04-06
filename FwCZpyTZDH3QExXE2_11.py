
def amount_fib(n):
  fNum = [0,1]
  c=0
  while fNum[-1] < n:
    ns = fNum[c] + fNum[c+1]
    fNum.append(ns)
    c+=1
  if n != 0:
    return len(fNum)-1
  else:
    return 0

