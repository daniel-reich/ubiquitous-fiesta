
def encrypt(key, message):
  swap = {}
  for a,b in zip(key[::2],key[1::2]):
    if a not in swap:
      swap[a] = b
    if b not in swap:
      swap[b] = a
  return ''.join(swap.get(i,i) for i in message)

