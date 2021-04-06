
import math
​
def get_number_of_apples(n, p):
  
  Number_Text = p.replace("%","")
  Number = int(Number_Text)
  Eaten = round(Number * 0.01, 2)
  Remaining = round(1 - Eaten,2)
  
  Children_Share = math.floor(n * Remaining)
  
  if (Children_Share == 0):
    return "The children didn't get any apples"
  else:
    return Children_Share

