
import datetime
​
def get_days(date1, date2):
  
  First = date1
  Second = date2
  
  Difference = date2 - date1
  
  Text = str(Difference)
  Blocks = Text.split(" ")
  Answer = int(Blocks[0])
  
  return Answer

