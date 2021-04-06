
def is_unfair_hurdle(hurdles):
  def determine_spacing(line):
    
    hash_indexes = []
    
    for n in range(len(line)):
      if line[n] == '#':
        hash_indexes.append(n)
    
    difs = []
    
    for n in range(len(hash_indexes) - 1):
      difs.append(hash_indexes[n+1] - hash_indexes[n])
    
    if difs.count(difs[0]) != len(difs):
      return difs
    
    else:
      return difs[0]
      
  
  if len(hurdles) >= 4:
    return True
  
  spacing = determine_spacing(hurdles[0])
  
  if spacing < 4:
    return True
  
  return False

