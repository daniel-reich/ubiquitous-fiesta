
def longest_slide(pyramid):
  curr = pyramid[-1]
  for i in range(len(pyramid)-2,-1,-1):
    curr = [max(a,b) for a,b in zip(curr,curr[1:])]
    curr = [a+b for a,b in zip(curr, pyramid[i])]
​
  return curr[0]

