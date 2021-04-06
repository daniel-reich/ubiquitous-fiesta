
def soroban(frame):
  top,bottom = frame[:2], frame[3:]
  total = 0
  for x,y in zip(range(1,8),top[1]):
    if y == "O":
      total += 5*10**(7-x)
  for i,x in zip(range(0,5),bottom):
    for y,z in zip(range(1,8),x):
      if z == "|":
        total += i*10**(7-y)
  return total

