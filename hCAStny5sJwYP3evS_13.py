
def is_early_bird(_range, n):
  s = ''.join(str(i) for i in range(_range+1))
  index = []
  for i in range(len(s)):
    if s.startswith(str(n), i):
      if n > 9 and n<100:
        index.append([i,i+1])
      if n>99 and n<1000:
        index.append([i,i+1,i+2])
  if len(index) > 1:
    index.append("Early Bird!")
    return index
  else:
    return index

