
def harry(po):
  if len(po[0])==0:
    return -1
  downright = sum(po[-1])+sum(po[i][0] for i in range(len(po)-1))
  rightdown = sum(po[0])+sum(po[i][-1] for i in range(len(po)-1))
  return max(downright,rightdown)

