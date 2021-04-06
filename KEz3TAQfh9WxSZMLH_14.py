
def count_all(txt):
  m={}
  ch,dig=0,0
  for x in txt:
    if x.isdigit():
      dig+=1
    elif 65<=ord(x)<=91 or 97<=ord(x)<=123:
      ch+=1
  m["LETTERS"]=ch
  m["DIGITS"]=dig
  return m

