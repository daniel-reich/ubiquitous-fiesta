
def convert_binary(string):
  return ''.join('0' if ord(c) < 78 else '1' for c in string.upper())

