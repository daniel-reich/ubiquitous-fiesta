
import decimal
​
def over_time(parameters):
​
  start = parameters[0]
  end = parameters[1]
  rate = parameters[2]
  factor = parameters[3]
    
  standard_time = 0
  over_time = 0
​
  over_time  += (min(9, end) - start) if start < 9 else 0
  over_time += (end - max(17, start)) if end > 17 else 0
  standard_time = min(17, end) - max(9, start)
  
  if standard_time < 0:
    standard_time = 0
  
  value = decimal.Decimal((standard_time * rate) + (over_time * rate * factor)).\
    quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_HALF_UP)
  return '${:04.2f}'.format(value)

