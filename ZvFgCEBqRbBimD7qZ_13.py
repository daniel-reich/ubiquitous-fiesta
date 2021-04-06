
def bowling(pins):
  frame = 0
  total = 0
  i = 0
  while(frame != 10):
    if pins[i] == 10:
      total = total + pins[i] + pins[i+1] + pins[i+2]
      i += 1
      frame += 1
    else:
      if(pins[i] + pins[i+1] == 10):
        total = total + pins[i] + pins[i+1] + pins[i+2]
        i += 2
        frame += 1
      else:
        total = total + pins[i] + pins[i+1]
        i += 2
        frame += 1
  return total

