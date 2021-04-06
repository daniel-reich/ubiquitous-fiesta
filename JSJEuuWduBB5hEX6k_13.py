
def XO(text):
  text = text.lower()
  num_x = text.count('x')
  num_o = text.count('o')
  
  return num_x == num_o
  
  if 'x' not in text and 'o' not in text:
    return True

