
def bit_rotate(n, m, d):
  b = bin(n)[2:]
  if d:
    return int(b[len(b)-m : ] + b[0 : len(b)-m], 2)
  else:
    return int(b[m :] + b[0 : m], 2)

