
def reversible_inclusive_list(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 2):
    Parameters.append([])
    Parameters.append(Parameters[0])
    Parameters.append(0)
  
  Start = Parameters[0]
  End = Parameters[1]
  Answer = Parameters[2]
  Cursor = Parameters[3]
  Added = Parameters[4]
  Required = abs(Start - End) + 1
  
  if (Added == Required):
    return Answer
  
  elif (Added < Required) and (Start > End):
    Answer.append(Cursor)
    Added += 1
    Cursor -= 1
    return reversible_inclusive_list(Start, End, Answer, Cursor, Added)
  
  elif (Added < Required) and (Start < End):
    Answer.append(Cursor)
    Added += 1
    Cursor += 1
    return reversible_inclusive_list(Start, End, Answer, Cursor, Added)
  
  else:
    return "ERROR"

