
def collatz(n):
  steps = 1
  highnum = 0
  seq = [n]
​
  for i in seq:
    if i % 2 != 0 and i != 1:
      seq.append((i * 3) + 1)
      steps += 1
      if ((i * 3) + 1) > highnum:
        highnum = ((i * 3) + 1)
    elif i % 2 == 0:
      seq.append(i/2)
      steps += 1
      if (i / 2) > highnum:
        highnum = (i / 2)
    else:
      seq.append(1)
      break
  return (steps, int(highnum))

