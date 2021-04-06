
def boom_intensity(n):
  if n < 2: return 'boom'
  s = 'B' + 'o' * n + 'm' + ('!' if n % 2 == 0 else '')
  return s.upper() if n % 5 == 0 else s

