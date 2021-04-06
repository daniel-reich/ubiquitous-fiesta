
def capital_letters(txt):
 upper = 0
 for i in range(len(txt)):
   if (ord(txt[i]) >= 65 and
     ord(txt[i]) <= 90):
      upper += 1
 return upper

