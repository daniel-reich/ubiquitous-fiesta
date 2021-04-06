
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
def double_swap(txt, c1, c2):
  a=find(txt,c1)
  b=find(txt,c2)
  txt=list(txt)
  for j in a:
    txt[j]=c2
  for k in b:
    txt[k]=c1
  return ''.join(txt)

