
def box_seq(step):
  n = 0
  for i in range(1,step + 1):
    if i % 2 == 1:
      n += 3
    else:
      n -= 1
  return n

