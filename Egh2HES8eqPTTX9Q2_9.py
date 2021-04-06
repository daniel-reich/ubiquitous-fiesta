
def convert(let,num):
  number1 = ord(let) - 97
  number2 = (num + number1) % 26
  number3 = number2 + 97
  return chr(number3)
  
def rolling_cipher(txt, n):
  letters = [convert(x,n) for x in txt]
  return ''.join(letters)

