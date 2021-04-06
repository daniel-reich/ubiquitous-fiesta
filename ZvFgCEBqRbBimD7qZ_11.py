
def bowling(pins):
  pass_next = False
  frames = []
  result = 0
  for i in pins:
    if pass_next:
      frames[-1].append(i)
      pass_next = False
    else:
      if i != 10:
        pass_next = True
      frames.append([i])
  for i in range(10):
    if frames[i][0] == 10:
      result += 10
      if len(frames[i+1]) == 2:
        result += sum(frames[i+1])
      else: 
        result += frames[i+1][0] + frames[i+2][0]
    elif sum(frames[i]) == 10:
      result += 10
      result += frames[i+1][0]
    else:
      result += sum(frames[i])
  return result

