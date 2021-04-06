
def longest_7segment_word(lst):
  lst = list(filter(lambda x: not any(c in x for c in 'kmvwx'), lst))
  return max(lst, key=len) if lst else ''

