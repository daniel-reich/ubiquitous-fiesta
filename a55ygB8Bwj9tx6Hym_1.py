
def steps_to_convert(txt):
  return min(len([x for x in txt if x.islower()]), len([x for x in txt if x.isupper()]))

