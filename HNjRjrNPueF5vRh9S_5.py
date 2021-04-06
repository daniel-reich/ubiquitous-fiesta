
class Base:
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_b10(self, val):
    
    vals = [1]
    expon = 1
​
    while max(vals) < val:
      vals.append(self.b ** expon)
      expon += 1
    
    vals = list(reversed(vals))
​
    digits = []
​
    for vl in vals:
      if vl > val:
        digits.append('0')
      else:
        digits.append(str(val // vl))
        val = val % vl
    
    tr = ''.join(digits)
​
    while len(tr) < 8:
      tr = '0' + tr
    
    return tr
​
def triple(bit):
  return bit.replace('0', '000').replace('1','111')
​
b2 = Base(2)
​
def hamming_code(msg):
​
  ascii_vals = [ord(l8r) for l8r in msg]
​
  bits = [b2.convert_from_b10(val) for val in ascii_vals]
​
  tripled = [triple(bit) for bit in bits]
​
  return ''.join(tripled)

