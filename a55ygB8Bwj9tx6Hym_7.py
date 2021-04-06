
def steps_to_convert(txt):
  countU = 0
  countL = 0
  for t in txt:
      if t.isupper():
          countU += 1
      if t.islower():
          countL += 1
  if countL > countU:
      return countU
  return countL

