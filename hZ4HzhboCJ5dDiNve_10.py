
def special_reverse_string(txt):
  stripped = ''
  for i in txt:
    if i != ' ':
      stripped += i
    reversed = stripped[::-1]
  output = ''
  for i in range(len(txt)):
    if txt[i] == ' ':
      output += ' '
    elif txt[i].islower():
      output += reversed[0].lower()
      try:
        reversed = reversed[1:]
      except:
        pass
    elif txt[i].isupper():
      output += reversed[0].upper()
      try:
        reversed = reversed[1:]
      except:
        pass
    else:
      output += reversed[0].lower()
      try:
        reversed = reversed[1:]
      except:
        pass
  return output

