
def frequency_sort(s):
  d = {}
  for c in s:
    d[c] = d.get(c, 0) + 1
  return ''.join([k * v for k, v in sorted(d.items(), key=lambda e: (-e[1], e[0]))])

