
def findOpening(brack):
  bracketPairs = [('(',')'),('<','>'),('[',']'),('{','}')]
  for a,b in  bracketPairs:
    if brack == b:
      return a
  return None
​
def bracket_logic(txt):
  openBrackets = ['(','<','[','{']
  closeBrackets = [')','>',']','}']
  stack = []  
  for i in range(len(txt)):
    if txt[i] in openBrackets:
      stack.append(txt[i])    
    if txt[i] in closeBrackets:
      openBrack = None
      try:
        openBrack = stack.pop() 
      except:
        return False
      if findOpening(txt[i]) != openBrack:
        return False
  
  if stack != []:
    return False
  return True

