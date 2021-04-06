
def bracket_logic(xp):
  brackets = ''.join(ch for ch in xp if ch in '()<>[]{}')
  
  dic = {'(': ')', '<': '>', '[': ']', '{': '}'}
  stack = []
  
  for i in brackets:
    if i in dic:
      stack.append(i)
    elif not stack or dic[stack.pop()] != i:
      return False
  
  return not stack

