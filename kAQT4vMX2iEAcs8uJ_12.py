
def longest_7segment_word(lst):
  import re
  ls=sorted(filter(lambda x : re.search(r"[kmvwx]",x)==None,lst),key=len,reverse=1)
​
  return '' if ls==[] else ls[0]

