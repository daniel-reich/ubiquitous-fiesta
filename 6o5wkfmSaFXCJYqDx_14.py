
def abcmath(a, b, c):
  for _ in range(b):
    a+=a
  return a%c==0

