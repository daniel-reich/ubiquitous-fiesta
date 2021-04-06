
def complete_binary(s):
  zero = ""
  while (len(s) + len(zero)) % 8 != 0:
    zero += "0"
  return zero + s

