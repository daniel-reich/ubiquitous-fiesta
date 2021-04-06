
def total_overs(balls):
  if balls%6==0:
    return balls/6
  else:
    return float("{}.{}".format(int(round((balls-balls%6)/6)),balls%6))

