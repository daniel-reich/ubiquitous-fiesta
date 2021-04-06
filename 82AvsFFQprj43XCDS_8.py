
import re
from collections import Counter
​
def no_strangers(txt):
  word_list = [i.lower() for i in re.findall(r'[a-z\']+',txt,re.I)]
  word = Counter(word_list)
  friend = [k for k,v in word.items() if v>= 5]
  # friend = [i[1] for i in friend]
  acq = [k for k,v in word.items() if 3<=v< 5]
  def sort_list(li,freq):
      sorted_list = []
      for i in li:
          counter = 0
          for ind, w in enumerate(word_list):
              if w == i:
                  counter += 1
                  if counter == freq:
                      sorted_list.append((ind,w))
                      break
      sorted_list = [i[1] for i in sorted(sorted_list)]
      return sorted_list
  return [sort_list(acq,3),sort_list(friend,5)]

