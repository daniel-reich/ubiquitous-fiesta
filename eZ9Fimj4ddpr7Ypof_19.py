
def mumbling(s):
  a = [i for i in range(1,len(s)+1)]
  b = [i for i in s]
  return "-".join([(j*i).capitalize() for (i,j) in zip(a,b)])

