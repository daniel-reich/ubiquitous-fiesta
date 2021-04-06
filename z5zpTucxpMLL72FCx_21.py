
def grab_city(txt):
  x = txt.split(']')[:-1]
  return (''.join(x)).split('[')[-1]

