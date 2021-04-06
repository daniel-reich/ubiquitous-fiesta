
def triple(word):
  result = ""
  for letter in word:
    result += letter * 3
  return result
def eight(num):
  return "{:0>8}".format(bin(num)[2:])
def hamming_code(message):
  return "".join(list(map(lambda letter: triple(eight(ord(letter))), message)))

