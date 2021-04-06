
def generate_nonconsecutive(n):
  return ' '.join(b[2:].zfill(n) for b in [bin(i) for i in range(2**n)] if not '11' in b)

