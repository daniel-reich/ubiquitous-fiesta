
def is_consecutive(s, start=None, d=0):
  if start is None:
    for i in range(1, len(s)):
      t = int(s[:i])
      if is_consecutive(s[i:], t + 1, 1) or is_consecutive(s[i:], t - 1, -1):
        return True
  else:
    if s == "":
      return True
    t = str(start)
    if s[:len(t)] == t and is_consecutive(s[len(t):], start + d, d):
      return True
  return False

