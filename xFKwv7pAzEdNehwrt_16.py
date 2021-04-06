
BRACKETS = {
')': '(',
']': '[',
'>': '<',
'}': '{'
}
​
def bracket_logic(xp):
  stack = []
  
  for c in xp:
    if c in BRACKETS.values():
      stack.append(c)
    elif c in BRACKETS.keys():
      if stack[-1] != BRACKETS[c]:
        return False
      stack.pop()
​
  return not stack

