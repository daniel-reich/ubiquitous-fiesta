
def longest_7segment_word(words):
  try:
    return max([w for w in sorted(words, key=len)
      if all(c not in 'kmvwx' for c in w)], key=len)
  except ValueError:
    return ''

