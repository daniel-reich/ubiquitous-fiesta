
def meme_sum(a, b):
  a = list(str(a))
  b = list(str(b))
  max_len = max(len(a), len(b))
  a = ['0']*(max_len - len(a)) + a
  b = ['0']*(max_len - len(b)) + b
​
  return int(''.join(str(int(a) + int(b)) for a,b in zip(a,b)))

