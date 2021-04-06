
def anagram(name, words):
  return sorted(''.join(words) + ' ') == sorted(name.lower())

