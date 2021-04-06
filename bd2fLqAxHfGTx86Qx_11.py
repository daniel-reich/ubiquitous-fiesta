
def can_complete(initial, word):
  removed_index = []
  for char in initial:
    if char in word:
      removed_index.append(word.index(char))
      word = word.replace(char,'', 1)
    else:
      return False
  return removed_index == sorted(removed_index)

