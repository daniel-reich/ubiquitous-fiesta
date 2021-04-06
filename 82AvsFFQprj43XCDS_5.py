
import re
​
def no_strangers(txt):
  counter = {}
  friends = []
  acquaintances = []
  pattern = re.compile(r"[\w']+", re.IGNORECASE)
  words = re.findall(pattern, txt)
​
  for word in words:
    word = word.lower()
    if word not in counter:
      counter[word] = 1
    else:
      counter[word] += 1
      if(counter[word]==3 and word not in acquaintances):
        acquaintances.append(word)
      if(counter[word]==5 and word not in friends):
        friends.append(word)
        acquaintances.remove(word)
          
​
  return [acquaintances, friends]

