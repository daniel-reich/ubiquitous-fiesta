
def even_odd_string(txt):
  even = ''
  odd = ''
  space = ' '
  for index, character in enumerate(txt):
    if(index%2 == 0):
      even = even + character
    else:
      odd = odd + character
  return  even + space + odd

