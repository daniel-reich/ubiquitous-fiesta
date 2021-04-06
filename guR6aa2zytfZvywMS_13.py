
def total_overs(balls):
  o,b=divmod(balls,6)
  return float(".".join(map(str,[o,b])))

