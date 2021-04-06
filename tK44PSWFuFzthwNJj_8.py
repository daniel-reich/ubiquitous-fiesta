
def club_entry(word):
  alphabet=[]
  password=0
  for i in range(97,123):
    alphabet.append(chr(i))
  for y in range(0,len(word)-1):
    if word[y]==word[y+1]:
      password+=(alphabet.index(word[y])+1)*4
  return password

