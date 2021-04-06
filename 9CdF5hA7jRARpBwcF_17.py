
from collections import defaultdict
def map_letters(word):
  dic = defaultdict(list)
  for i,w in enumerate(word):
    dic[w].append(i)
  return dic

