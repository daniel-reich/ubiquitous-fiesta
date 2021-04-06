
def digital_decipher(eMessage, key):
  base = ord('a') - 1
  key_index = 0
  key = str(key)
  result = []
  for char in eMessage:
    result.append(chr(char - int(key[key_index]) + base))
    key_index = (key_index + 1) % len(key)
  return ''.join(result)

