
def bowling(pins,r=0):
  if r == 10: return 0
  if pins[0]+pins[1] < 10:
    return pins[0]+pins[1] + bowling(pins[2:],r+1)
  if pins[0]+pins[1] == 10 and pins[0]<10:
    return pins[0]+pins[1]+pins[2] + bowling(pins[2:],r+1)
  if pins[0]==10:
    return pins[0]+pins[1]+pins[2] + bowling(pins[1:],r+1)

