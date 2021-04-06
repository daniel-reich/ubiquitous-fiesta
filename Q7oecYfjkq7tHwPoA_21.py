
def climb(stamina, obstacles):
  ret = 0
  up = False
  for i in range(len(obstacles)-1):
    if obstacles[i]>obstacles[i+1]:
      up = False
    else:
      up = True
    temp = abs(obstacles[i]-obstacles[i+1])
    if temp%1>0:
      temp = temp//1+1
    if up:
      temp*=2
    if temp<=stamina:
      stamina-=temp
      ret+=1
    else:
      return ret
  return ret

