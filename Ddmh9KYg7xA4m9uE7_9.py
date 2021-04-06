
def convert_binary(string):
  nystr = string.lower()
  return ''.join(['0' if i in 'abcdefghijklm' else '1' for i in nystr])

