
def can_complete(initial, word):
  index = 0
  for c in word:
    if c == initial[index]:
      index += 1
      if index >= len(initial):
        return True
  return False

