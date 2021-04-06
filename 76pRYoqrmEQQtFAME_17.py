
def is_astonishing(n):
  s = str(n)
  for i in range(1, len(s)):
    a, b, m = int(s[:i]), int(s[i:]), n
    for x in range(max(a, b), min(a, b)-1, -1):
      m -= x
      if m < 0:
        break
    if not m:
      return '{}-Astonishing'.format('AB' if a < b else 'BA')
  return False

