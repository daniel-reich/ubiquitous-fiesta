
def text_to_number_binary(txt):
  toReturn = []
  for x in txt.lower().split(): 
    if x == 'zero': toReturn.append('0')
    elif x == 'one': toReturn.append('1')
  while (len(toReturn) % 8 != 0): 
    toReturn.pop(-1)
  return "".join(toReturn)

