
def pop(state):
  
  # Checking to see if 'state' are all zeroes
  
  Total = sum(state)
  
  if (Total == 0):
    return state
  
  # Checking to see where non-zero item is
  
  Position = 0
  Counter = 0
  Length = len(state)
  
  while (Counter < Length):
    
    Item = state[Counter]
    
    if (Item == 0):
      Counter += 1
    else:
      Position = Counter
      Counter += 1
  
  # Amending Values 
  
  Cursor_A = Position - 1
  Cursor_B = Position + 1
  Value = state[Position] - 1
  Length = len(state)
  
  while (Value > 0):
    
    if (Cursor_A >= 0) and (Cursor_B < Length):
      state[Cursor_A] = Value
      state[Cursor_B] = Value
      Value -= 1
      Cursor_A -= 1
      Cursor_B += 1
  
    elif (Cursor_A >= 0) and (Cursor_B >= Length):
      state[Cursor_A] = Value
      Value -= 1
      Cursor_A -= 1
  
    elif (Cursor_A < 0) and (Cursor_B < Length):
      state[Cursor_B] = Value
      Value -= 1
      Cursor_B += 1
  
    else:
      Cursor_A -= 1
      Cursor_B += 1
  
  # Giving Answer
  return state

