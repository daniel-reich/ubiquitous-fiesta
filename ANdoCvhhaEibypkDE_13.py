
def closing_in_sum(n):
  n = str(n)
  m = len(n)//2
  s = sum(int(x+y) for x, y in zip(n[:m],n[m:][::-1]))
  return  s if not len(n) % 2 else s + int(n[m])

