
def decode(txt):
  return [sum(map(int, str(ord(letter)))) for letter in txt]

