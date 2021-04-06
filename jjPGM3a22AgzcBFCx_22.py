
def decrypt(lst):
  c = list(range(1, 26))
  for x in c:
    if x not in lst:
      d = x
  return chr(d + 64)

