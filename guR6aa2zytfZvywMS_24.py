
def total_overs(balls):
  o, b = divmod(balls, 6)
  return o + b/10 if b else o

