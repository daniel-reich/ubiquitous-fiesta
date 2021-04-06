
def get_items_at(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 2):
    Parameters.append([])
    Parameters.append(1)
    
  Sample = Parameters[0]
  Wanted = Parameters[1]
  Answer = Parameters[2]
  Instance = Parameters[3]
  
  if (Sample == []):
    return Answer
  
  elif (Instance % 2 == 0) and (Wanted == "even"):
    Answer.insert(0, Sample[-1])
    Sample = Sample[0:-1]
    Instance += 1
    return get_items_at(Sample, Wanted, Answer, Instance)
  
  elif (Instance % 2 != 0) and (Wanted == "odd"):
    Answer.insert(0, Sample[-1])
    Sample = Sample[0:-1]
    Instance += 1
    return get_items_at(Sample, Wanted, Answer, Instance)
    
  else:
    Sample = Sample[0:-1]
    Instance += 1
    return get_items_at(Sample, Wanted, Answer, Instance)

