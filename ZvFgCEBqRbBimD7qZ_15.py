
def bowling(pins):
  ball = 0
  frame = 0
  total = 0
  while frame < 10:
    if pins[ball] == 10:
      total = total + 10 + pins[ball + 1] + pins[ball + 2]
      ball += 1
    elif (pins[ball] + pins[ball+1]) == 10:
      total = total + 10 + pins[ball+2]
      ball += 2
    else:
      total = total + pins[ball] + pins[ball+1]
      ball += 2
    frame += 1
  return total

