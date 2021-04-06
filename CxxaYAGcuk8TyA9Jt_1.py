
from collections import deque
def checkBalance(s):
  stack = deque([])
  count = 0
  if not s: return -1
  if not set(')}') & set(s): return len(s) 
  
  for char in s:
​
    if char == '(' or char == '{':
      stack.append(char)
​
    elif char == ')':
      if stack:
        if stack.pop() != '(':
          return count
      else: return count
​
    elif char == '}':
      if stack:
        if stack.pop() != '{':
          return count
      else: return count
​
    count += 1
​
  return len(s) if stack else -1

