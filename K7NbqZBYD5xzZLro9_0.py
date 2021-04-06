
def digits_sum(start, stop, a=0):
  import sys
  sys.setrecursionlimit(100000000)
  if start == stop+1:
    return a
  else:
    b=sum(int(i) for i in str(start))
    return digits_sum(start+1, stop, a+b)

