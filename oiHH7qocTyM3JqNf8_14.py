
def move(word):
  s=""
  for x in word:
    if x.islower():
      if ord(x) < 122:
        s=s+chr(ord(x)+1)
      else:
         s=s+'a'
    else:
      if ord(x) < 90:
        s=s+chr(ord(x)+1)
      else:
         s=s+'A'
  return s

