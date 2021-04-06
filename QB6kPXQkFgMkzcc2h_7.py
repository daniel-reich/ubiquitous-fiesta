
def remove_abc(txt):
  txt1=''
  for i in txt:
    if i.lower()=='a' or i.lower()=='b' or i.lower()=='c':
      continue
    else:
      txt1=txt1+i
  return None if txt1==''or txt1==txt else txt1

