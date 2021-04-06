
def convert_to_decimal(perc):
  return [float(i.strip("%"))*0.01 for i in perc]

