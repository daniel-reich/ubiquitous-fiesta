
def bracket_logic(xp):
  valid = True;
  scope = []
  obrackets = list("(<[{")
  cbrackets = list(")>]}")
  # () <> [] {}
  for i in xp:
    if (i in obrackets):
      scope.append(i)
    elif (i in cbrackets):
      if (not chr(ord(i)-[2, 1][i == ")"]) == scope[-1]):
        print(chr(ord(i)-[2, 1][i == ")"]))
        valid = False;
        break;
      else:
        del scope[-1]
  if (len(scope)):
    valid = False;
  return valid

