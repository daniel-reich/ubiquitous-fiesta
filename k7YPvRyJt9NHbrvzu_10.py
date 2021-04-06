
def count(lst,score,n):
  if score == 0:
    return 1
  elif score < 0:
    return 0
  elif n <= 0 and score > 0:
    return 0
  else:
    return count(lst,score,n-1) + count(lst, score - lst[n-1], n)
​
def football(score):
  return count([2,3,6,7,8],score,5)

