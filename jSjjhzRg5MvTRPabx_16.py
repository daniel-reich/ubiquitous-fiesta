
def sentence(Sample):
  
  Sentence = ""
  Vowels = "aeiuo"
  
  Counter = 0
  Length = len(Sample)
  Last = Length - 1
  
  while (Counter < Length):
    
    Word = Sample[Counter]
    Initial = Word[0]
    
    if (Counter == 0) and (Initial in Vowels):
      Sentence = Sentence + "An " + Word
      Counter += 1
    elif (Counter == 0) and (Initial not in Vowels):
      Sentence = Sentence + "A " + Word
      Counter += 1
    
    elif (Counter == Last) and (Initial in Vowels):
      Sentence = Sentence + " and an " + Word + "."
      Counter += 1
    elif (Counter == Last) and (Initial not in Vowels):
      Sentence = Sentence + " and a " + Word + "."
      Counter += 1
    
    elif (Initial in Vowels):
      Sentence = Sentence + ", an " + Word
      Counter += 1
    elif (Initial not in Vowels):
      Sentence = Sentence + ", a " + Word
      Counter += 1
      
    else:
      Counter += 1
​
  return Sentence

