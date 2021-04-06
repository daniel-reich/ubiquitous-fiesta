
def generate_rug(n):
  m = n // 2
  return [[max(abs(x - m), abs(y - m)) for x in range(n)] for y in range(n)]

