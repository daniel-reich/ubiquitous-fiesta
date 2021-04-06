
def steps_to_convert(txt):
  return min(sum(1 for x in txt if x.isupper()), sum(1 for x in txt if x.islower()))

