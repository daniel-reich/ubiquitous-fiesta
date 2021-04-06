
def min_turns(current, target):
  ans = 0
  for i in range(0, len(current)):
    f = abs(int(current[i]) - int(target[i]))
    s = 10 - f
    ans += min(f, s)
  return ans

