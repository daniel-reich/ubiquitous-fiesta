
def secret(num):
  
  Text = str(num)
  
  First = int(Text[0])
  Second = int(Text[1])
  
  Part_01 = First ** Second
  Part_02 = First * Second
  Answer = Part_01 - Part_02
  
  return Answer

