
class Base:
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_b10(self, b10_val):
​
    values = [1]
    expon = 1
​
    while max(values) < b10_val:
      values.append(self.b ** expon)
      expon += 1
    #print(values)
    values = list(reversed(values))
    
    tr_vals = []
​
    for value in values:
      if value <= b10_val:
        tr_vals.append(b10_val//value)
        b10_val = b10_val % value
      else:
        tr_vals.append(0)
    
    while tr_vals[0] == 0:
      tr_vals.pop(0)
​
    return tr_vals
​
  def convert_to_b10(self, base_value):
​
    values = [1]
    expon = 1
​
    while len(values) < len(base_value):
      values.append(self.b ** expon)
      expon += 1
    
    values = list(reversed(values))
​
    return sum([values[n] * base_value[n] for n in range(len(values))])
​
b128 = Base(128)
​
​
def int_to_vlq(n):
  try:
    converted = b128.convert_from_b10(n)
  except IndexError:
    return [0]
  return [converted[n] + 128 for n in range(len(converted) - 1)] + [converted[-1]]
def vlq_to_int(lst):
​
  converted = b128.convert_to_b10([lst[n] - 128 for n in range(len(lst) - 1)] + [lst[-1]])
​
  return converted

