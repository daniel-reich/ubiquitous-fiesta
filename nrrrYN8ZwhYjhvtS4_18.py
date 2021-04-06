
def extend_vowels(word, num):
  s=""
  l=["a","e","i","o","u","A","E","I","O","U"]
  if num==0:
    return word
  elif num%1==0 and num>0:
    for i in word:
      if i in l:
        s=s+i*(num+1)
      else:
        s=s+i
    return s
  else:
    return "invalid"

