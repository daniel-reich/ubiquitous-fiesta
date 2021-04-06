
def remap(value, low1, high1, low2, high2):
  h,i,j=value-low1,high1-low1,high2-low2
  return 0 if high1-low1==0 else low2+(j/(i/h)) if low1>high1 or low2>high2 or low2<0 else (j/(i/h))

