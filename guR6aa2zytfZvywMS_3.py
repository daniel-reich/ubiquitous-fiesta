
def total_overs(balls):
  overs=balls//6
  ball=balls%6
  if ball==0:
    return overs
  else:
    return overs+ball/10

