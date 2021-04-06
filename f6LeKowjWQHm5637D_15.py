
def cap_to_front(s):
  cap = ""
  for x in s:
    if x == x.upper():
      cap += x
  for y in s:
    if y == y.lower():
      cap += y
  return cap

