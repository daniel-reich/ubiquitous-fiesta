
def atbash(txt):
  al='abcdefghijklmnopqrstuvwxyz'
  alc=al.upper()
  alr=al[::-1]
  alcr=alc[::-1]
  dic1={}
  for i in range(26):
    dic1[al[i]]=alr[i]
  dic2={}
  for j in range(26):
    dic2[alc[j]]=alcr[j]
  final=''
  for  k in txt:
    if k in al:
      final+=dic1[k]
    elif k in alc:
      final+=dic2[k]
    else:
      final+=k
  return final

