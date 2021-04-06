
def generate_rug(n):
  mid = n // 2
  return [[max(abs(mid - r), abs(mid - c)) for c in range(n)] for r in range(n)]

