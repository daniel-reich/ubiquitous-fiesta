
dif_ciph = lambda x: [ord(c)-ord(x[i-1])
  if i else ord(c) for i, c in enumerate(x)] \
  if type(x) == str else ''.join(chr(sum(x[:i+1]))
  if i else chr(n) for i, n in enumerate(x))

