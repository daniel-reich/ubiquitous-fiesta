
import re
def check_balance(expression):
  pairs = {"{":"}","(":")","[":"]"}
  closed = False
  left = []
  current = None
  for i, char in enumerate(expression):
    if char in pairs.keys():
      if current:
        left.append(current)
      current = char
    elif char in pairs.values():
      if not current:
        return i
      elif pairs[current] == char:
        if left:
          current = left[-1]
          left.pop()
        else:
          current = None    
      else:
        return i
  return len(expression) if current else -1

