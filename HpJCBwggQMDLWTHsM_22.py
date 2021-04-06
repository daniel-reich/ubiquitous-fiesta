
def average_word_length(txt):
  
  Sample = str(txt)
  
  Blocks = Sample.split(" ")
  Words = len(Blocks)
  
  Letters = 0
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item = Sample[Counter]
    
    if (Item.isalpha()):
      Letters += 1
      Counter += 1
    else:
      Counter += 1
  
  Answer = round(Letters/Words, 2)
  
  return Answer

