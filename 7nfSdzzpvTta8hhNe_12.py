
def organize(txt):
  
  if (txt == ""):
    return {}
  
  Dictionary = {}
  
  Sample = str(txt)
  Sample = Sample.replace(", ",",")
  Blocks = Sample.split(",")
  
  Key1 = "name"
  Value1 = Blocks[0]
  Dictionary[Key1] = Value1
  
  Key2 = "age"
  Value2 = int(Blocks[1])
  Dictionary[Key2] = Value2
  
  Key3 = "occupation"
  Value3 = Blocks[2]
  Dictionary[Key3] = Value3
  
  return Dictionary

