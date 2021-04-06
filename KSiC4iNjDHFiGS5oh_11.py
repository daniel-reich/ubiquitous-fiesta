
def is_super_d(n):
  for i in range(2, 10):
    num = list(str(i * (n ** i)))
    count = 0
    for c in num:
      if c == str(i):
        count += 1
        if count == i: return "Super-{} Number".format(i)
      else:
        count = 0
​
  return "Normal Number"

