
def missing_letter(txt):
  txt=[chr(ord(i)+1) for i,j in zip(txt,txt[1:]) if ord(j)-ord(i)!=1]
  return txt[0] if len(txt)==1 else 'No Missing Letter'

