
def remap(value, low1, high1, low2, high2):
​
  
  if low1 == high1 \
    or high1 == high2:
    return 0
  else:
    return low2+(high2-low2)*((value-low1)/(high1-low1))

