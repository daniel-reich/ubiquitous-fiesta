
def find_difference(a, b):
  l1,w1,h1 = a
  l2,w2,h2 = b
  return abs((l1*w1*h1)-(l2*h2*w2))

