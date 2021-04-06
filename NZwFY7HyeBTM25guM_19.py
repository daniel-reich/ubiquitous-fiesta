
def convert_to_decimal(perc):
  myList = [float(perc[e][:-1])/100 for e,i in enumerate(perc)]
  return myList

