
def magic(txt):
  val = [int(i) for i in txt.split(" ")]
  if val[0] * val[1] == int(txt[-1]):
    return True
  elif val[0] * val[1] == int(txt[-2:]):
    return True
  else:
    return False

