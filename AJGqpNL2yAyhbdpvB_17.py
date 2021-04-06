
def adc(value):
  b=(value+1)/204.8
  print(b)
  if str(b*1000).split(".")[0][-1] in "56":
    return round(b-0.005,2)
  return round(b,2)

