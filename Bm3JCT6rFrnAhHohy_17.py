
def alphabet_index(txt):
  string=""
  for i in txt:
    if (ord(i)>=65 and ord(i)<=90):
      string+=str(ord(i)-64)+" "
    if(ord(i)>=97 and ord(i)<=122):
      string+=str(ord(i)-96)+" "
  return string.strip()

