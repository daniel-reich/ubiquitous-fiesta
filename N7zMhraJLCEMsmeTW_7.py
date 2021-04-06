
def min_swaps(s):
​
  swps0 = sum( 1 for i in range(len(s)) if s[i] != '0101010101'[i]   )
  swps1 = sum( 1 for i in range(len(s)) if s[i] != '0101010101'[i+1] )
​
  return min(swps1,swps0)

