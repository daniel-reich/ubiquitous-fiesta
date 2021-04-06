
def bugger(num):
  o = 0
  while num >= 10:
    j = 1
    for i in str(num):
      j *= int(i)
    num = j
    o += 1
  return o

