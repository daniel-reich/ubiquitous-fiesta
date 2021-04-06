
def meme_sum(a, b):
  a = list(reversed(str(a)))
  b = list(reversed(str(b)))
  ans = ''
  for i in range(0, max(len(a), len(b))):
    A, B = 0, 0
    if i < len(a):
      A = int(a[i])
    if i < len(b):
      B = int(b[i])
    for j in reversed(str(A + B)):
      ans += j
  return int(ans[::-1])

