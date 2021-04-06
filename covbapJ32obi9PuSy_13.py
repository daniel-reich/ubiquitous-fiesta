
def diamond_arrays(x):
  a=[[i]*i for i in range(1,x+1)]
  return a+a[-2::-1]

