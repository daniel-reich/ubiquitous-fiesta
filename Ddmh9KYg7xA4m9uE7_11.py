
def convert_binary(string):
  string = string.lower()
  result = ''
  for i in range(len(string)):
    if ord(string[i]) < 110:
      result += '0'
    else:
      result += '1'
  return result

