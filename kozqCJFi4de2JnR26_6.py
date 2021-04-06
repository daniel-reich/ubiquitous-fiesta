
def fib_str(n, txt):
  ans = [txt[0],txt[1]]
  for i in range(n-1):
    ans.append(ans[-1]+ans[-2])
  return ', '.join(ans[:n])

