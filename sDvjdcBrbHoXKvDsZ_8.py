
def anagram(name, words):
  return sorted(name.lower().replace(" ", "")) == sorted("".join(words))

