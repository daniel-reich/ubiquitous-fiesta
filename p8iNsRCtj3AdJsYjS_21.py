
def title_to_number(s):
  
  Code = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  Power = 0
  Text = str(s)
  
  Total = 0
  
  while (Text != ""):
    
    Letter = Text[-1]
    Place = Code.index(Letter)
    Score = Place * (26 ** Power)
    Total += Score
    
    Text = Text[0:-1]
    Power += 1
    
  return Total

