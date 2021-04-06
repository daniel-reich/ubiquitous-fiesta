
def encrypt(key, message):
  lst=[key[i-1]+key[i-2] if i%2 == 0 else key[i-1]+key[i] for i in range(len(key),0,-1)]
  d = dict(lst)
  return ''.join(d.get(i, i) for i in message)

