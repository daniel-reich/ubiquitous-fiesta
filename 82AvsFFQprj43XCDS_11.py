
from collections import Counter
import re
​
def no_strangers(txt):
  txt = txt.lower()
  punctuation = r'[.,!?"]'
  txt = re.sub(punctuation, '', txt).split(' ')
​
  acquaintance = []
  friend = []
  cnt = Counter()
  for word in txt:
    cnt[word]+=1
    if cnt[word]==3:
      acquaintance.append(word)
    if cnt[word]==5:
      acquaintance.remove(word)
      friend.append(word)
  return [acquaintance, friend]

