
def convert_binary(string):
  return ''.join(['1','0'][97<=ord(i)<=109] for i in string.lower())

