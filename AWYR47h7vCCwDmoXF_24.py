
def is_goal_scored(goal):
  
  Counter = 0
  Length = len(goal)
  
  Failsafe = 0  
  Horizontal = 0
  
  # Establishing Position of Horizontal Bar
  
  while (Counter < Length) and (Failsafe == 0):
    
    Item = str(goal[Counter])
    Test = Item.count("#")
    
    if (Test > 2):
      Horizontal = Counter
      Failsafe += 1
      Counter += 1
    else:
      Counter += 1
  
  # Establishing if Zero is in between Vertical Bars
  
  Counter = 0
  End = Horizontal
  
  while (Counter < End):
    
    Item = str(goal[Counter])
    
    if ("0" in Item):
      Aspect_A = Item.index("#")
      Aspect_B = Item.rindex("#")
      Aspect_C = Item.index("0")
      
      if (Aspect_C > Aspect_A) and (Aspect_C < Aspect_B):
        return True
      else:
        return False
    
    else:
      Counter += 1
  
  return False

