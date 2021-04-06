
def is_valid(txt):
  counts = sorted(txt.count(c) for c in set(txt))
  if len(set(counts)) == 1: return "YES"
  counts[-1] -= 1
  return "YES" if len(set(counts)) == 1 else "NO"

