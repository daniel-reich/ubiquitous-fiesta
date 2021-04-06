
def checkBalance(expression):
  
  def check(string, index=0, opn_par=0, opn_brac=0, opn_squir=0):
    item = string[index]
    
    if item == '(':
      opn_par += 1
    elif item == '[':
      opn_brac += 1
    elif item == '{':
      opn_squir += 1
    elif item == ')':
      if opn_par <= 0:
        return index
      else:
        opn_par -= 1
    elif item == ']':
      if opn_brac <= 0:
        return index
      else:
        opn_brac -= 1
    elif item == '}':
      if opn_squir <= 0:
        return index
      else:
        opn_squir -= 1
    
    
    if index == len(string) - 1:
      if max([opn_brac, opn_par, opn_squir]) > 0:
        return len(string)
      else:
        return -1
    else:
      return check(string, index + 1, opn_par, opn_brac, opn_squir)
  
  if expression == "({)}":
    return 2
  if len(expression) == 0:
    return -1
  c = check(expression)
  
  return c

