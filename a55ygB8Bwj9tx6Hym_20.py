
def steps_to_convert(txt):
  a = sum([1 for i in txt if i.isupper()])
  b = sum([1 for i in txt if i.islower()])
  if a == b:
    return a or b
  elif a > b:
    return b
  elif a < b:
    return a

