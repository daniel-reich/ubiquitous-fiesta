
def reverse_title(txt):
  words = txt.split(' ')
  output = ''
  for word in words:
    output += word[0].lower()
    output += word[1:].upper()
    output += ' '
  return output[:-1]

