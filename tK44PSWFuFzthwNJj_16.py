
def club_entry(word):
  i = 0
  x = len(word)
  if word[i] == word[1+i]:
    y =((ord(word[i])-96)*4)
  else:
    while i < x:
      if word[i] == word[1+i]:
        break
      i+=1
      y =((ord(word[i])-96)*4)
  return(y)

