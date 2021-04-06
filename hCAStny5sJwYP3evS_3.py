
def is_early_bird(_range, n):
  seq = "".join(map(str, range(_range + 1)))
  n = str(n)
​
  pos = []
  i = -1
​
  while True:
    i = seq.find(n, i + 1)
    if i == -1:
      break
    else:
      pos.append(list(range(i, i + len(n))))
​
  if len(pos) >= 2:
    pos.append("Early Bird!")
​
  return pos

