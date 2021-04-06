
def vigenere(text, key):
  alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
  alpha = [i for i in alpha]
​
  alphaMatrix = []
​
  for i in range(len(alpha)//2):
      alphaMatrix.append(alpha[i:26+i])
​
​
  if text != text.upper():
    text = [i.upper() for i in text if i.upper() in alpha]
    text = "".join(text)
    length = len(text)
    key = key.upper()
    mult = (length // len(key)) + 1
    key = key * mult
    message = ""
    for i in range(length):
        if text[i] not in alpha:
          continue
        c = alpha.index(text[i])
        r = alpha.index(key[i])
        letter = alphaMatrix[r][c]
        message += letter
    return message
  else:
    length = len(text)
    key = key.upper()
    mult = (length // len(key)) + 1
    key = key * mult
    message = ""
    for i in range(length):
      r = alpha.index(key[i])
      letter = alphaMatrix[r].index(text[i])
      letter = alpha[letter]
      message += letter
    return message

