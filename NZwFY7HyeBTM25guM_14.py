
def convert_to_decimal(perc):
  for idx,value in enumerate(perc):
    perc[idx] = float(value.replace("%",""))/100
  return perc

