
def get_sequence(low, high):
  
  List = []
  
  Value = low
  Ceiling = high
  
  while (Value <= Ceiling):
    List.append(Value)
    Value +=1
  
  return List

