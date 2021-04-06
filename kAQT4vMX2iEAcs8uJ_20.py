
def longest_7segment_word(lst):
  lst = [w for w in lst if not set(w)&set('kmvwx')]
  return '' if not lst else max(lst, key=len)

