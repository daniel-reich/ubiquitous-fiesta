
def longest_7segment_word(lst):
  lst = [x for x in lst if all(c not in 'kmvwx' for c in x)]+['']
  return max(lst, key=len)

