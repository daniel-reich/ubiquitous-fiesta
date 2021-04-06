
def digit_count(n):
  res = ""
  n = str(n)
  for i in n:
    res += str(n.count(i))
  return int(res)

