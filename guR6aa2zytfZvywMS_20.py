
def total_overs(balls):
  if balls % 6 == 0:
    return (balls // 6) 
  else: 
    return (balls // 6) + ((balls % 6) / 10)

