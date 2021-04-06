
def no_duplicate_letters(phrase):
  words = phrase.split(" ")
  for word in words:
    for i in range(len(word)):
      for j in range(i):
        if word[i]==word[j]:
          return False
  return True

