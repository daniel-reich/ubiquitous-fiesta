
def anagram(name, words):
  first_words = name.split(" ")
  return sorted((''.join(first_words)).lower()) == sorted(''.join(words))

