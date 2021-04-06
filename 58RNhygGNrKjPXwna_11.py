
def longest_nonrepeating_substring(txt):
​
  Counter = 0
  Length = len(txt)
​
  Current = 0
    
  Word = ""
  Target = txt[0]
  
  while (Current < Length):
        
    if (Word == ""):    
      Word = Word + txt[Current]
      Current += 1
        
    elif (txt[Current] in Word):
        
      if (len(Word) > len(Target)):
        Target = Word
        Counter += 1
        Current = Counter
        Word = ""
      else:
        Counter += 1
        Current = Counter
        Word = ""
    
    else:
      Word = Word + txt[Current]
      Current += 1
​
  if (len(Word) > len(Target)):
    Target = Word
​
  return Target

