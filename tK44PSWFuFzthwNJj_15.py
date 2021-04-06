
def club_entry(word):
  return 4 * (ord([word[x] for x in range(len(word)) if word[x] == word[x-1]][0]) - 96)

