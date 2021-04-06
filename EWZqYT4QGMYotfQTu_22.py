
def tap_code(text):
  alpha = ['abcde','fghij','lmnop','qrstu','vwxyz']
  out=''
  if text[0].isalpha(): #Cypher
    for i in text:
      if i == 'k': i = 'c'
      for a in alpha:
        if i in a:
          let = [alpha.index(a)+1, a.index(i)+1]
          break
      out += '.'*let[0] + ' ' + '.'*let[1] + ' '
  else: #Decypher
    text += ' '
    count = 0
    code = []
    for i in text:
      if i == '.': count += 1
      else:
        code.append(count)
        count = 0
    for i in zip(code[::2], code[1::2]):
      out+= alpha[i[0]-1][i[1]-1]
  return out.strip()

