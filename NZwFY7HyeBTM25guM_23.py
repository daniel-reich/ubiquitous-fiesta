
def convert_to_decimal(perc):
  return list(map(lambda x: float(x.strip('%'))/100, perc))

