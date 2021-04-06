
def int_to_vlq(n, has_more=False):
  bits = n & 0b01111111
  n >>= 7
  rest = int_to_vlq(n, True) if n else []
  if has_more:
    bits += 128
  rest.append(bits)
  return rest   
  
def vlq_to_int(lst):
  v = 0
  for byte in lst:
    v <<= 7
    v |= (byte & 0b01111111)
  return v

