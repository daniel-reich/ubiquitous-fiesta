
def group(l,s):
  x = 1+(len(l)-1)//s
  return [[l[i*x+j] for i in range (1+(len(l)-j-1)//x)] for j in range (x)]

