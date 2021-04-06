
def vigenere(text, keyword):
  cipher = [[chr(x) for x in range(65,91)][i:] + [chr(x) for x in range(65,91)][:i] for i in range(0,26)]
  txt = "".join([x.upper() for x in text if x.isalpha()])
  keyword = "".join([keyword[x%(len(keyword))].upper() for x in range(len(txt))])
  result = ""
  
  if text.isupper():
    for i in range(len(txt)):
      x = ord(keyword[i]) - 65
      y = cipher[x].index(txt[i])
      result += cipher[0][y]
    return result
​
  for i in range(len(txt)):
    x, y = ord(txt[i]) - 65, ord(keyword[i]) - 65
    result += cipher[x][y]
  return result

