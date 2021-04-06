
def bracket_logic(xp):
  brackets = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
  }
  stack = list()
  for char in xp:
    if char in brackets.keys():
      stack.append(char)
    elif char in brackets.values():
      if brackets[stack.pop()] != char:
        return False
  return len(stack) == 0

