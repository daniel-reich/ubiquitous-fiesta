
def gimme_the_letters(spectrum):
  alphabet = ''.join([chr(i) for i in range(97, 123)])
​
  if spectrum[0].isupper():
    alphabet = alphabet.upper()
​
  a, b = alphabet.index(spectrum[0]), alphabet.index(spectrum[-1])
  
  return alphabet[a:b+1]

