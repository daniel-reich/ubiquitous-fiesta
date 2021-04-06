
def pentagonal(num):
  dot_min_1=1
  for i in range(1,num+1):
    dot=dot_min_1+5*(i-1)
    dot_min_1=dot
  return(dot)

