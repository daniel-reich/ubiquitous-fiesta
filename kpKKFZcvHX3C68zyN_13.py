
def swap_cards(n1, n2):
  
  # Establishing Elements...
  
  Paul_Current_Hand = str(n1)
  Paul_Current_First = Paul_Current_Hand[0]
  Paul_Current_Second = Paul_Current_Hand[1]
  
  Opponent_Current_Hand = str(n2)
  Opponent_Current_First = Opponent_Current_Hand[0]
  Opponent_Current_Second = Opponent_Current_Hand[1]
  
  # Establishing What to Swap...
  
  Paul_First_Number = int(Paul_Current_Hand[0])
  Paul_Second_Number = int(Paul_Current_Hand[1])
  
  if (Paul_Second_Number < Paul_First_Number):
    
    Paul_New_Hand = Paul_Current_First + Opponent_Current_First
    Paul_New_Number = int(Paul_New_Hand)
    
    Opponent_New_Hand = Paul_Current_Second + Opponent_Current_Second
    Opponent_New_Number = int(Opponent_New_Hand)
    
  else:
    
    Paul_New_Hand = Opponent_Current_First + Paul_Current_Second
    Paul_New_Number = int(Paul_New_Hand)
    
    Opponent_New_Hand = Paul_Current_First + Opponent_Current_Second
    Opponent_New_Number = int(Opponent_New_Hand)
  
  # Establishing Result...
  
  if (Paul_New_Number > Opponent_New_Number):
    return True
  else:
    return False

