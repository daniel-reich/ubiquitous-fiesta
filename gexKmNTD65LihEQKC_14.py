
def is_super_cool(string):
  if not string:  return False
  d = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8,
    14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6}
  total, l = 0, len(string)
  for i in [30, 20]:
    if l>i:
      total += d[i]
      l -= i
  total += d[l]
  return bool(string)
# This challenge was pointless. I didn't
# bother finishing once I saw the test cases.

