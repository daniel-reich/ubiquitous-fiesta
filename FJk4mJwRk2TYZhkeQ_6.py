
def accum(txt):
  s = str()
  count = 0
  for letter in txt:
    s = s + letter.upper() + letter.lower() * count + '-'
    count += 1
  return s.rstrip('-')

