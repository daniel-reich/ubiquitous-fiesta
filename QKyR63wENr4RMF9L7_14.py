
def tweak_letters(word,lst):
 newlis= [j+k for j,k in zip(lst,[ord(i) for i in word])]
 for n,i in enumerate(newlis):
  if i==123:
   newlis[n]=97
  elif i==96:
   newlis[n]=122
 return "".join([chr(i) for i in newlis])

