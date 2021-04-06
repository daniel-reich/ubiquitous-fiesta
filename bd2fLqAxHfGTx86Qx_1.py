
def can_complete(initial, word):
  stack = list(initial)[::-1]
  for letter in word:
    if letter == stack[-1]: stack.pop()
  return not stack

