
def keyword_cipher(key, message):
  alph = ''.join(chr(i) for i in range(97,123))
  
  key_new=''
  for j in key:
    if key_new.count(j) == 0:
      key_new += ''.join(j)
  
  alph1 = alph
  for k in key:
    alph1 = alph1.replace(k,'')
  
  trans_tab = message.maketrans(alph, key_new + alph1)
  return message.translate(trans_tab)

