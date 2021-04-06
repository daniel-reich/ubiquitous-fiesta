
def steps_to_convert(txt):
  lower = len([i for i in txt if i.islower()])
  upper = len([i for i in txt if i.isupper()])
  return min(lower, upper)

