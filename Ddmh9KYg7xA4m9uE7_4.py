
def convert_binary(string):
  return ''.join(['0' if 'a' <= l.lower() <= 'm' else '1' for l in string])

