
def time(dct, people, walls):
  rate = dct["walls"]/(dct["minutes"]*dct["people"])
  return round(walls/(rate*people))

