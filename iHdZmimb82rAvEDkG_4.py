
def bitwise_index(r):
  x, k = (float("-inf"), -1)
  for i, n in enumerate(r): x, k = [(x, k), (n, i)][(n > x) & ~(n & 1)]
  return [{'@'+['even', 'odd'][k & 1]+' index '+str(k): x}, 'No even integer found!'][k < 0]

