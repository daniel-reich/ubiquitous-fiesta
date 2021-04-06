
def generate_rug(n, direction):
  if direction == 'left':
    l1 = [y for y in range(n)]
    l2 = [y for y in range(1,1+n)][::-1]
    return [l2[x:] + l1[:x] for x in range(n,0,-1)]
  else:
    l1 = [y for y in range(n)][::-1]
    l2 = [y for y in range(1,1+n)]
    return [l1[x:] + l2[:x] for x in range(n)]

