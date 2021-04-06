
import re
def no_strangers(txt):
  mem = {}
  words = re.split('[^\w\']+', txt.lower())
  for i,word in enumerate(words):
    if word not in mem:
      mem[word] = {'count':0}
    mem[word]['count'] += 1
    if mem[word]['count'] in (1,3,5):
      mem[word]['index'] = i
  
  acquaintance = []
  friend = []
  for word in mem:
    if 2 < mem[word]['count'] < 5: acquaintance.append(word)
    elif mem[word]['count'] >= 5: friend.append(word)
    mem[word] = mem[word]['index']
  return [sorted(group, key = mem.get) for group in (acquaintance, friend)]

