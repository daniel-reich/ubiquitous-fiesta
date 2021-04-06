
def digital_decipher(eMessage, key):
  cipher = str(key) * len(eMessage)
  result = [eMessage[i] - int(cipher[i]) for i in range(len(eMessage))]
  return ''.join([chr(let+96) for let in result])

