
def digital_decipher(msg, key):
  key = str(key)
  l = len(msg) // len(key) + 1
  key = (key * l)[:len(msg)]
  ret = [i - int(j) for i, j in zip(msg, key)]
  return "".join(chr(c+ord('a')-1) for c in ret)

