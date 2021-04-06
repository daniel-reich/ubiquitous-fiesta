
def alternating_caps(txt):
  up = 0
  new = ""
  for i in txt:
    if i.isalpha():
      up += 1
    if up % 2 == 1:
      new += i.upper()
    else:
      new += i.lower()
  return new

