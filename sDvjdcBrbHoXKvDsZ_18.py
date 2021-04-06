
def anagram(name, words):
  name = name.lower().split(' ')
  name = ''.join(name); 
  name = [i for i in name]
  name.sort()
  words = ''.join(words)
  words = [j for j in words]
  words.sort()
  return ''.join(name) == ''.join(words)

