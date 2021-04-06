
def convert_binary(string):
  return ''.join(['0' if ord(n) in range(ord('a'),ord('m')+1) else '1' for n in string.lower()])

