
def anagram(name, words):
  name = name.lower().replace(' ','')
  words = ''.join(words)
  return sorted([i for i in name]) == sorted([i for i in words])

