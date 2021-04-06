
def remove_repeats(txt):
  s = ''
  for char in txt:
    if char != s[-1:]:
      s = s + char
  return s

