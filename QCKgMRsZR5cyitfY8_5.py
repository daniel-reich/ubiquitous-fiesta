
def get_type(v):
  x = str(type(v)).split(" ")[-1]
  y = x.strip(">").strip("'")
  return y

