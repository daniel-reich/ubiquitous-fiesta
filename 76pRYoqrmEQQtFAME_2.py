
def is_astonishing(n):
  s = str(n)
  for i in range(1, len(s)):
    a, b = int(s[:i]), int(s[i:])
    o = b < a
    if o: a, b = b, a
    if (a + ~b) * (a + b) == -2 * n:
      return ['AB','BA'][o] + '-Astonishing'
  return 0

