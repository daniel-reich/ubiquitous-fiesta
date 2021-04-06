
def power_ranger(poww, minn, maxx):
  return len([i for i in range(minn, maxx+1) if i**(1/poww)%1==0])

