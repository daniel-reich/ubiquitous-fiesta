
def validate_binary(b):
  ones = sum(1 for n in b[:-1] if n == '1') % 2
  last = b[-1]
  return ones < 1 and last == '0' or ones and last == '1'

