
def convert_binary(string):
  result = ''
  for ch in string.lower():
    if ord(ch) in range(ord('a'), ord('n')):
      result += '0'
    elif ord(ch) in range(ord('n'), ord('{')):
      result += '1'
    else:
      raise ValueError('Non-alpha character is not allowed.')
  return result

