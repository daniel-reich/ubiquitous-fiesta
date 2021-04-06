
def digital_cipher(message, key):
  res = []
  str_key = str(key)
  for i in range(0,len(message)):
    key_unit = int(str_key[i % len(str_key)])
    res.append(ord(message[i]) - 96 + key_unit)
  return res

