
letters = "abcdefghijklmnopqrstuvwxyz".upper()
codes = []
for x in range(len(letters)):
  codes.append([letters[i] for i in range(len(letters))])
  letters = letters[1:] + letters[0]
  
def vigenere(text, keyword):
  t = "".join([x for x in text if x.upper() in letters]).upper()
  key = keyword * (len(t)//len(keyword)) + keyword[:(len(t)%len(keyword))]
  column = [codes[x][0] for x in range(len(codes))]
  sol = ""
  if text.upper() == text and "".join(text.split()) == text:
    for t_letter, k_letter in zip(t, key):
      for x in range(len(codes)):
        if codes[x][codes[0].index(k_letter.upper())] == t_letter:
          sol += column[x]
    return sol
  else:
    for t_letter, k_letter in zip(t, key):
      sol += codes[column.index(k_letter.upper())][codes[0].index(t_letter)]
    return sol

