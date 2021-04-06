
def steps_to_convert(txt):
  cap = 0
  low = 0
  for item in txt:
    if 65 <= ord(item) <= 90:
      cap += 1
    else:
      low += 1
  if cap < low:
    return cap
  else:
    return low

