
from string import ascii_letters as al
def club_entry(word):
  char = ""
  for x in range(len(word)-1):
    if word[x] == word[x+1]:
      char = word[x]
  return (al.index(char)+1)*4

