
def edabit_in_string(txt):
  t = iter("edabit")
  cur = next(t)
  for c in txt:
    if c == cur:
      try:
        cur = next(t)
      except StopIteration:
        return 'YES'
  return 'NO'

