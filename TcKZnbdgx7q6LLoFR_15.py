
def collect(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 2):
    Answer = []
    Parameters.append(Answer)
  
  Sample = Parameters[0]
  Divider = Parameters[1]
  Answer = Parameters[2]
  
  Batch = Sample[0:Divider]
  
  if (len(Batch) == Divider):
    Answer.append(Batch)
    return collect(Sample[Divider:], Divider, Answer)
  else:
    return sorted(Answer)

