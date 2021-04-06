
def divide(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 2):
    Parameters.append(0)
    Parameters.append(abs(Parameters[0]))
    Parameters.append(abs(Parameters[1]))
  
  Value_A = Parameters[0]
  Value_B = Parameters[1]
  Answer = Parameters[2]
  Remaining = Parameters[3]
  Divisor = Parameters[4]
​
  if (Remaining % Divisor != 0):
    Excess = Remaining % Divisor
    Remaining -= Excess
    return divide(Value_A, Value_B, Answer, Remaining, Divisor)
  
  elif (Value_A == 0):
    return Answer
  elif (Remaining == 0) and (Value_A > 0) and (Value_B > 0):
    return Answer
  elif (Remaining == 0) and (Value_A < 0) and (Value_B < 0):
    return Answer
  
  elif (Remaining == 0) and (Value_A > 0) and (Value_B < 0):
    return Answer * -1
  elif (Remaining == 0) and (Value_A < 0) and (Value_B > 0):
    return Answer * -1
    
  else:
    Remaining -= Divisor
    Answer += 1
    return divide(Value_A, Value_B, Answer, Remaining, Divisor)

