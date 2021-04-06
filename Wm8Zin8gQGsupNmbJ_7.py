
def binary_conversion(txt):
  if txt != "":
    n = int(txt, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
  else:
    return ""

