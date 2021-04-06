
def char_index(word, char):
  if char not in word:
    return None
  x = [idx for idx, ch in enumerate(word) if ch == char]
  first = min(x)
  last = max(x)
  return [first, last]

