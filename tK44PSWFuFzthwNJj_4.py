
def club_entry(word):
  alpha="abcdefghijklmnopqrstuvwxyz"
  for i in range(len(word)-1):
    if word[i] == word[i+1]:
      key = word[i]
  return 4*(alpha.find(key)+1)

