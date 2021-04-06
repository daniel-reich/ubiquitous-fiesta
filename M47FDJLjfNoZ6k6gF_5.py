
def cup_swapping(swaps):
  cups = [0, 1, 0]
  for s in swaps:
    a = ord(s[0]) - 65
    b = ord(s[1]) - 65
    cups[a], cups[b] = cups[b], cups[a]
  return "ABC"[cups.index(1)]

