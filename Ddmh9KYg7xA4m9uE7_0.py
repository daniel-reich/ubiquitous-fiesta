
def convert_binary(string):
  return ''.join(str(int(x > 'm')) for x in string.lower())

