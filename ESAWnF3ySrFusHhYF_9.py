
############################################################
#   Sub Function
############################################################
​
def FNC_Word_Tweaker(Sample):
​
  if (Sample == ""):
    return "-"
  
  Length = len(Sample)
  
  if (Length % 2 == 0):
    Middle = int(Length / 2)
  else:
    Middle = int((Length + 1)/2)
    
  Sample = Sample.upper()
  Sample = Sample[::-1]
  
  Front = Sample[0:Middle]
  Back = Sample[Middle:]
  
  Output = Front + "-" + Back
  return Output
​
############################################################
#   MAIN FUNCTION
############################################################
​
def edit_words(lst):
  
  Answer = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    Word = lst[Counter]
    New = FNC_Word_Tweaker(Word)
    Answer.append(New)
    Counter += 1
  
  return Answer

