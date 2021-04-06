
def min_turns(current, target):
  lst1 = [int(x) for x in current]
  lst2 = [int(x) for x in target]
  sum = 0
​
  for i in range(4):
    mx = max(lst1[i], lst2[i])
    mn = min(lst1[i], lst2[i])
    sum += min(mx-mn, mn+10-mx)
​
  return sum

