
############################################################
#     Sub Function 1
############################################################
​
def FNC_Deck_Builder(Number):
​
  Card = 1
  Deck = []
  
  while (Card <= Number):
    Deck.append(Card)
    Card += 1
    
  return Deck
​
############################################################
#     Sub Function 2
############################################################
​
def FNC_Shuffle_Process(Deck):
  
  Middle = int(len(Deck) / 2)
  
  Batch_A = Deck[Middle:]
  Batch_B = Deck[1:Middle]
  
  Shuffled = []
  
  Counter = 0
  Length = len(Batch_B)
  
  while (Counter < Length):
    
    Card_A = Batch_A[Counter]
    Shuffled.append(Card_A)
​
    Card_B = Batch_B[Counter]
    Shuffled.append(Card_B)
​
    Counter += 1
    
  Shuffled.append(Batch_A[-1])
  Shuffled.insert(0, Deck[0])
  
  return Shuffled
​
############################################################
#     MAIN FUNCTION
############################################################
​
def shuffle_count(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Target = FNC_Deck_Builder(Parameters[0])
    Revised = FNC_Deck_Builder(Parameters[0])
    Parameters.append(Target)
    Parameters.append(Revised)
    Shuffles = 0
    Parameters.append(Shuffles)
  
  Size = Parameters[0]
  Target = Parameters[1]
  Revised = Parameters[2]
  Shuffles = Parameters[3]
  
  Revised = FNC_Shuffle_Process(Revised)
  
  if (Revised == Target):
    Shuffles += 1
    return Shuffles
  else:
    Shuffles += 1
    return shuffle_count(Size, Target, Revised, Shuffles)

