
def digital_decipher(eMessage, key):
  res = ""
  str_key = str(key)
  for i in range(len(eMessage)):
    no = eMessage[i] - int(str_key[i % len(str_key)])
    ch = chr(96 + no % 26)
    res += ch
  return res

