
def steps_to_convert(txt):
  up = sum(x.isupper() for x in txt)
  low = sum(x.islower() for x in txt)
  return min(up,low)

