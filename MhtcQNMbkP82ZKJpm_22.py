
import operator
​
def get_notes_distribution(students):
  
  # Extracting All the Scores from the Dictionaries
  
  Scores = []
  
  Counter = 0
  Length = len(students)
  
  while (Counter < Length):
    Item = students[Counter]
    Marks = Item["notes"]
    Scores.extend(Marks)
    Counter += 1
  
  # Establishing Valid Scores
  
  Valid = []
  
  Counter = 0
  Length = len(Scores)
  
  while (Counter < Length):
    Item = Scores[Counter]
    
    if (Item >= 1) and (Item <= 5) and (Item % 1 == 0):
      Valid.append(Item)
      Counter += 1
    else:
      Counter += 1
  
  # Establishing Unique Valid Scores
  
  Unique = set(Valid)
  Unique = list(Unique)
  Unique = sorted(Unique)
  
    # Establishing Frequencies of Unique Scores
  
  Frequencies = []
  
  Counter = 0
  Length = len(Unique)
  
  while (Counter < Length):
    Item = Unique[Counter]
    Events = Valid.count(Item)
    Frequencies.append(Events)
    Counter += 1
  
  # Building Dictionary
  
  Dictionary = {}
  
  FC = 0
  FL = len(Frequencies)
  
  UC = 0
  UL = len(Unique)
  
  while (FC < FL) and (UC < UL):
    Key = Unique[UC]
    Value = Frequencies[FC]
    Dictionary[Key] = Value
    FC += 1
    UC += 1
  
  # Sorting Dictionary by Values
  Dictionary = dict(sorted(Dictionary.items(), key=operator.itemgetter(1), reverse=True))
  
  # Giving Answer
  return Dictionary

