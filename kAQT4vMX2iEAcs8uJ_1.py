
def longest_7segment_word(lst):
  for word in sorted(lst, key=len, reverse=True):
    if all([ True if x not in "kmvwx" else False for x in word ]):
      return word
  return ""

