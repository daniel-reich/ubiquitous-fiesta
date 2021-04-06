
def digital_decipher(message, key):
  sage = tuple(map(int, str(key)))
  length = len(sage)
  return ''.join(
    chr(num - sage[index % length] + 96)
    for index, num in enumerate(message)
  )

