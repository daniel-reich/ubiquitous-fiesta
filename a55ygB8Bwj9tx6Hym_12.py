
def steps_to_convert(txt):
  if txt.islower() or txt.isupper() or txt == "":
    return 0
  upper = len([i for i in txt if i.isupper()])
  lower = len([i for i in txt if i.islower()])
  return min(upper, lower)

