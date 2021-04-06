
def bitwise_logical_negation(x):
  x=x|(x>>8)
  x=x|(x>>4)
  x=x|(x>>2)
  x=x|(x>>1)
  return (x&1)^1

