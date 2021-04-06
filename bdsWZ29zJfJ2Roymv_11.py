
def swap_two(txt):
  chars = list(txt)
  new = []
  i = 0
  while i < len(chars)-3:
    new.extend([chars[i+2], chars[i+3]])
    new.extend([chars[i], chars[i+1]])
    i += 4
  tail = len(txt)%4
  if tail > 0:
    chunk = chars[-tail:]
    new.extend(chunk)
  s = ''.join(new)
  return s

