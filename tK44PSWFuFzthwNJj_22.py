
def club_entry(word):
  for i in word: 
    if i*2 in word:
      return (ord(i)-ord("a")+1)*4

