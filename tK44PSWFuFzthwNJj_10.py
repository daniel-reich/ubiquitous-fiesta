
def club_entry(word):
    i=0
    while i<len(word)-1:
          if word[i]==word[i+1]:return (ord(word[i])-96 )*4
          i+=1

