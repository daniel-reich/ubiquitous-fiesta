
import random
​
def gen_deck():
  
  Cards = []
  Values = []
  Suits = []
  
  Numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  Number_Cursor = 0
  Number_Span = len(Numbers)
  
  Branches = ["c","d","h","s"]
  Branch_Cursor = 0
  Branch_Span = len(Branches)
  
  while (Number_Cursor < Number_Span) and (Branch_Cursor < Branch_Span):
    
    while (Number_Cursor < Number_Span):
      
      Front = Numbers[Number_Cursor]
      Values.append(Front)
      Back = Branches[Branch_Cursor]
      Suits.append(Back)
      Number_Cursor += 1
      
    Number_Cursor = 0
    Branch_Cursor += 1
  
  Build = zip(Values, Suits)
  Cards = list(Build)
  
  return Cards

