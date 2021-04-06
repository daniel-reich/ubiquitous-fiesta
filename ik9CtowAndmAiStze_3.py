
def frequency_sort(s):
  return "".join(sorted(s, key=lambda c: (-s.count(c), 0 if c.isupper() else 1, c)))

