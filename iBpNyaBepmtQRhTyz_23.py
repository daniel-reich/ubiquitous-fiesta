
def c_cipher(msg, keyword):
​
  ciphertext = []
  lmsg = ''.join(ch.lower() for ch in msg if ch.isalnum())
  skeyword = sorted(keyword)
  wordlen = len(keyword)
  wordhei = len(lmsg)//wordlen
  
  if wordlen*wordhei < len(lmsg):
    wordhei += 1
    
  ret = ''
  
  if ' ' in msg:    #encrypt
    for _ in range(wordhei):
      ciphertext.append(['x'] * wordlen)\
      
    for i in range(len(lmsg)):
      ciphertext[i//wordlen][i%wordlen] = lmsg[i]
      
    fliped = [i for i in zip(*ciphertext)]
    
    for l in skeyword:
      ret += ''.join(ch for ch in fliped[keyword.index(l)])
  else:             #decrypt
    for _ in range(wordlen):
      ciphertext.append(['x'] * wordhei)
      
    omsg = ''
    for l in keyword:
      omsg += lmsg[skeyword.index(l) * wordhei:(skeyword.index(l)+1) * wordhei]
​
    for i in range(len(ciphertext)):
      for j in range(wordhei):
        ciphertext[i][j] = omsg[i * wordhei + j]
        
    fliped = [i for i in zip(*ciphertext)]
    
    for r in fliped:
      ret += ''.join(ch for ch in r)
      
  return ret

