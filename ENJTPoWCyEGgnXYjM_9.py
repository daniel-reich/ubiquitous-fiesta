
def percent_filled(box):
  empty = sum(a.count(' ') for a in box )
  full = sum(a.count('o') for a in box )
  return str(int(full/(full+empty)*100)) + '%'

