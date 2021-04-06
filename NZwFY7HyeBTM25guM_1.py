
def convert_to_decimal(perc):
  return [float(item.strip("%")) * .01 for item in perc]

