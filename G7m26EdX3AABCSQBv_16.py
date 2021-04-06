
def format_ascii(txt, width):
  result = ""
  for i, letter in enumerate(txt):
    if(i % width == 0) & (i > 0):
      result += '\n'
    result += letter
  return result

