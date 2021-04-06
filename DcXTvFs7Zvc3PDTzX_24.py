
def validate_binary(b):
  parity_bit = b[:-1]
  parity_bit_ones_count = parity_bit.count("1")
  if parity_bit_ones_count % 2 == 0:
    if b[-1] == "0":
      return True
    else:
      return False
  if parity_bit_ones_count % 2 != 0:
    if b[-1] == "1":
      return True
    else:
      return False

