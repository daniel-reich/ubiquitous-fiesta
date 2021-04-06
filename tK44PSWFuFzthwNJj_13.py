
def club_entry(word):
  for i in range(len(word)):
    if word[i] == word[i+1]:
      return (ord(word[i]) - 96) * 4

