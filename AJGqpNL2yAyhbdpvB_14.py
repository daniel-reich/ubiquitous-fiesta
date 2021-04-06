
def adc(value):
  
  one_volt = 1023/5
  one_adc = 1/one_volt
  
  return round(value * one_adc,2)

