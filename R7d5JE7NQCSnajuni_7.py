
def convert_to_number(dictionary):
  
  Revised = {}
  
  Fronts = []
  Backs = []
  
  for key, value in dictionary.items():
    Fronts.append(key)
    Backs.append(value)
    
  Counter = 0
  Length = len(Fronts)
  
  while (Counter < Length):
    Key = str(Fronts[Counter])
    Value = int(Backs[Counter])
    Revised[Key] = Value
    Counter += 1
    
  return Revised

