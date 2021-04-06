
def sort_word(word):
  upper = [ch for ch in word if ch.isupper()]
  lower = [ch for ch in word if ch.islower()]
  return "".join(sorted(upper)) + "".join(sorted(lower))

