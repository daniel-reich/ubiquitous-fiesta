
def bracket_logic(xp):
  open_brackets = ["[","{","(","<"]
  closed_brackets = ["]","}",")",">"]
  status_brackets = []
  for i in range(0,len(xp)):
    if xp[i] in open_brackets:
      status_brackets.append(xp[i])
    elif xp[i] in closed_brackets:
      if len(status_brackets) == 0:
        return False
      elif open_brackets.index(status_brackets[-1]) == closed_brackets.index(xp[i]):
        status_brackets.pop(-1)
      else:
        return False
  return bool(len(status_brackets) == 0)

