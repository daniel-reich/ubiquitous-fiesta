
def check_balance(expression):
  closing_to_opening = {
    '}': '{',
    ')': '(',
  }
  stack = []
  for index, char in enumerate(expression):
    if char in ('(', '{'):
      stack.append(char)
    if (char in (')', '}') 
      and (
        not stack or stack.pop() != closing_to_opening[char]
      )
    ):
      return index
  if stack:
    return len(expression)
  return -1

