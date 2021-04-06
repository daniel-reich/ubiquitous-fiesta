
def last_name_lensort(names):
  
  Surnames = []
  
  Counter = 0
  Length = len(names)
  
  while (Counter < Length):
    Full = names[Counter]
    Blocks = Full.split(" ")
    Surnames.append(Blocks[1])
    Counter += 1
  
  Surnames = sorted(Surnames, key = lambda x : (len(x), x))
  
  Revised = []
  
  Taken = 0
  
  NC = 0
  NL = len(names)
​
  SC = 0
  SL = len(Surnames)
  
  while (NC < NL) and (SC < SL):
    Wanted = Surnames[SC]
    Checking = names[NC]
    
    if (Wanted in Checking):
      Revised.append(Checking)
      SC += 1
      NC = 0
    else:
      NC += 1
  
  return Revised

