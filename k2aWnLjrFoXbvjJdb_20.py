
at=[chr(65+x) for x in range(26)]
vt=[[at[x+i if x+i<26 else x+i-26] for x in range(26)] for i in range(26)]
def vigenere(s,k):
  if ' ' not in s and '.' not in s:
    input_is_msg=False
  else:
    input_is_msg=True
  sp=''.join(list(map(lambda x: x if x.isalpha() else '',list(s.upper()))))
  k=k.upper()
  kp=k*(len(sp)//len(k))+k[0:len(sp)%len(k)]
  if input_is_msg:
    return ''.join([vt[ord(sp[i])-65][ord(kp[i])-65] for i in range(len(sp))])
  else:
    return ''.join([at[vt[ord(kp[i])-65].index(sp[i])] for i in range(len(sp))])

