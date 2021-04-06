
def condi_cipher(message, key, shift):
  alph=''.join(chr(i+97) for i in range(26))
  alph_1=sorted(alph, key=lambda x: (key+alph).index(x))
  d=dict(enumerate(alph_1))
  inv_d={i:j for j,i in d.items()}
  s=''
  for i in message:
    if i.isalpha():
      num=(inv_d[i]+shift)%26
      let=d[num]
      shift=inv_d[i]+1
      s+=let
    else:
      s+=i
  return s

