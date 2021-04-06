
def time(dct, people, walls):
  tr = dct["people"] * dct["minutes"] / dct["walls"]
  return  tr * walls / people

