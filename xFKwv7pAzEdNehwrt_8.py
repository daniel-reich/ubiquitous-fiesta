
def bracket_logic(xp):
  brackets = list(xp)
  bracketlist = []
  for bracket in brackets:
    if bracket == '<' or bracket == '{' or bracket == '(' or bracket == '[':
      bracketlist.append(bracket)
    elif bracket == '>' or bracket == '}' or bracket == ')' or bracket == ']':
      if len(bracketlist) > 0:
        popped = bracketlist.pop()
        if bracket == ')':
          if popped != '(':
            return False
        elif ord(popped) != (ord(bracket)-2):
          return False
      else:
        return False
  if len(bracketlist) != 0:
    return False
  return True

