
def longest_7segment_word(lst):
  try:
    return sorted([i for i in lst if all(x not in 'kmvwx' for x in i)], key=len, reverse=True)[0]
  except:
    return ""

