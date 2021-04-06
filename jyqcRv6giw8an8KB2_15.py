
def invert(s):
  s = s[::-1]
  output = ''
  for i in s:
    if i.isupper():
      output += i.lower()
    else:
      output += i.upper()
  return output

