
############################################################
#     Sub Function
############################################################
​
def FNC_Comparison_Tool(Word, Template):
​
  if (len(Word) != len(Template)):
    return False
  
  Counter = 0
  Length = len(Word)
  
  while (Counter < Length):
    Item_A = Word[Counter]
    Item_B = Template[Counter]
    
    if (Item_A == Item_B):
      Counter += 1
    elif (Item_B == "*"):
      Counter += 1
    else:
      return False
  
  return True
​
############################################################
#     MAIN FUNCTION
############################################################
​
def scrambled(words, mask):
  
  Wanted = []
  
  Counter = 0
  Length = len(words)
  
  while (Counter < Length):
    
    Template = str(mask)
    Word = words[Counter]
    
    if (FNC_Comparison_Tool(Word, Template)):
      Wanted.append(Word)
      Counter += 1
    else:
      Counter += 1
  
  return Wanted

