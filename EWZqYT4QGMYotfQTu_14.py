
def tap_code(text):
  #Define letter and code arrays
  letters = [chr(x) for x in range(97, 123) if x != 107]
  code = [("."*x + " " + "."*y) for x in range(1,6) for y in range(1,6)]
  
  if text.find('.') == -1: #If letter string
    text = ''.join(i if i != 'k' else 'c' for i in text) #Substitute k for c
    return ' '.join(code[letters.index(i.lower())] for i in text)
  else:
    split_pts = [i for i, j in enumerate(text) if j == ' '][1::2] #Index of every other ' '  character
    text = ''.join(text[i] if i not in split_pts else '@' for i in range(0,len(text))) #Replace with @
    return ''.join(letters[code.index(i)] for i in text.split('@'))

