
def no_strangers(txt):
  txt = ''.join(
    char for char in txt.lower() if char not in r'",.')
​
  words = txt.split()
  counter = {word: 0 for word in words}
  acquaintances, friends = [], []
  
  for word in words:
    counter[word] += 1
    if counter[word] == 3:
      acquaintances.append(word)
    if counter[word] == 5:
      friends.append(word)
      acquaintances.remove(word)
      
  return [acquaintances, friends]

