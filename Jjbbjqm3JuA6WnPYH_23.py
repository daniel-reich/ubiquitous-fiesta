
def bit_rotate(n, m, d):
  if d:
    binary = bin(n).replace("0b","")
    m = m%len(binary)
    return int(binary[-m:] + binary[:-m], 2)
  else:
    binary = bin(n).replace("0b","")
    m = m%len(binary)
    return int(binary[m:] + binary[:m], 2)

