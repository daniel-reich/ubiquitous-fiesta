
def number_split(n):
  half=int(n/2)
  if half+half==n:
    return [half,half]
  if half>=0:
    half1=half+1
  else:
    half1=half-1
  a=[half,half1]
  if n>=0:
    return a
  else:
    return [min(half,half1),max(half,half1)]

