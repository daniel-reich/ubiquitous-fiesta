
def find_longest(sentence):
  
  # Converting Sentence to Lower Case
  Sample = sentence.lower()
  
  # Establishing 'Allowed' Letters
  # (to filter out punctuation)
  Allowed = " abcedefghijklmnopqrstuvwxyz"
  
  # Bucket for Punctuation Free Sentence
  Revised = ""
  
  # Extracting Non-Punctuation Items
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item = Sample[Counter]
    
    if (Item in Allowed):
      Revised = Revised + Item
      Counter += 1
    else:
      Revised = Revised + " "
      Counter += 1
  
  # Splitting Revised into Word Blocks
  Blocks = Revised.split(" ")
  
  # Buckets for Answer
  Answer = ""
  Target = 0
  
  # Establishing Longest Word
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    Item = Blocks[Counter]
    Span = len(Item)
    
    if (Span > Target):
      Answer = Item
      Target = Span
      Counter += 1
    else:
      Counter += 1
  
  # Giving Answer
  return Answer

