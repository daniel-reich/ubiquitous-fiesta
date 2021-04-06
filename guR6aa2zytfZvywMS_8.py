
def total_overs(balls):
  nBalls = divmod(balls,6)[0]
  overs = divmod(balls,6)[1]
  return nBalls if overs ==0 else float(str(nBalls)+'.'+str(overs))

