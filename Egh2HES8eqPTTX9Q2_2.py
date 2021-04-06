
def rolling_cipher(txt, n):
  lets = 'abcdefghijklmnopqrstuvwxyz'
  result = ''
  
  for char in txt:
    result += lets[(lets.index(char)+n)%26]
  
  return result

