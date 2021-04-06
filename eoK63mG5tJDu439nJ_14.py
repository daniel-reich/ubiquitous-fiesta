
def isWordChain(words):
  is_chain = False
  for i in range(len(words)-1):
    s1 = words[i]
    s2 = words[i+1]
    num_hit = num_hits(s1, s2)
    if len(s2) == len(s1) + 1 and num_hit == len(s1):
      is_chain = True
    elif len(s2) == len(s1) - 1 and num_hit == len(s1) - 1:
      is_chain = True
    elif len(s2) == len(s1) and num_hit == len(s1) - 1:
      is_chain = True
    else:
      return False
  return is_chain
​
def num_hits(s1, s2):
    num_hit = 0
    for char in s1:
        if char in s2:
            num_hit += 1
    return num_hit

