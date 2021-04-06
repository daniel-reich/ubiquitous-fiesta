
def nico_cipher(message, key):
  index = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
  lk, lm = len(key), len(message)
  n = int(lm / lk)
  r = lk - lm % lk
  msgs = [list(message[i * lk : i * lk +lk]) for i in range(n)]
  msgs += [list(message[n * lk:]) + [' ']*r]
  return ''.join([msg[i] for msg in msgs for i in index])

