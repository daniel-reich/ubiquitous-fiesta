
def remove_repeats(s):
  y = []
  for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
      y += [s[x]]
  return "".join(y) + s[-1]

