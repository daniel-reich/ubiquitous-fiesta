
def no_duplicate_letters(phrase):
  wordlist = phrase.split()
  print(wordlist)
  for word in wordlist:
    if len(word) > len(set(word)):
      return False
  return True

