
def football(score):
  out = 0
  for i in range(1 + score//2):
    for j in range(1 + score//3):
      for k in range(1 + score//6):
        for l in range(1 + score//7):
          for m in range(1 + score//8):
            if score == i*2 + j*3 + k*6 + l*7 + m*8:
              out+=1
  return out

