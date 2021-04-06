
def func(num):
  s = str(num)
  i = 0
  for c in s:
    i += int(c)
  return i - (len(s) ** 2)

