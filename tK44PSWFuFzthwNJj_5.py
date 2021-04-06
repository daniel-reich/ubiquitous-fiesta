
def club_entry(word):
  abc = "abcdefghijklmnopqrstuvwxyz"
  for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
      return (abc.index(word[i].lower()) + 1) * 4

