
def missing_alphabets(txt):
  a=[]
  for i in range(26):
    a.append(chr(97+i))
  n=len(txt)//len({i for i in txt}) if len(txt)%len({i for i in txt})==0 else len(txt)//len({i for i in txt})+1
  a = sorted([i for i in a]*n)
  for i in txt:
    a.remove(i)
  return "".join(a)

