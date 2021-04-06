
def bowling(pins):
  frames = [0]*10
  i = 0
  pins = pins + [0]*(24-len(pins))
​
  for frame in range(10):
    frames[frame] += pins[i] + pins[i+1]
    if pins[i] == 10: # strike
      frames[frame] += pins[i+2]
    elif (pins[i] + pins[i+1]) == 10: # spare
      frames[frame] += pins[i+2]
      i += 1
    else:
      i += 1
    i += 1
    
  return sum(frames)

