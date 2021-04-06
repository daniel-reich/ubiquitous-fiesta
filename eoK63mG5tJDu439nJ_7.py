
def get_prefix_length(long, short):
  prefix = 0
  while prefix < len(short) and long[prefix] == short[prefix]:
    prefix += 1
  return prefix
    
def linkable(s1, s2):
  if len(s2) > len(s1):
    s1, s2 = s2, s1
  prefix_len  = get_prefix_length(s1, s2)
  suffix_len  = get_prefix_length(s1[::-1], s2[::-1])
  return len(s1) - (suffix_len + prefix_len) <= 1 
  
​
def isWordChain(words):
  return all(linkable(w1, w2) for w1, w2 in zip(words, words[1:]))

