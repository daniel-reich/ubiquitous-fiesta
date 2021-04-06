
def grab_city(txt):
  return txt.replace("]","").split("[")[-1]

