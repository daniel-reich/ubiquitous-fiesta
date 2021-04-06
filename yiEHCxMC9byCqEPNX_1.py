
def is_palindrome(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Forwards = ""
    Parameters.append(Forwards)
    Backwards = ""
    Parameters.append(Backwards)
    
  Sample = Parameters[0].lower()
  Forwards = Parameters[1]
  Backwards = Parameters[2]
  
  if (Sample == "") and (Forwards == Backwards):
    return True
  elif (Sample == "") and (Forwards != Backwards):
    return False
  elif (Sample[0].isalpha()):
    Forwards = Forwards + Sample[0]
    Backwards = Sample[0] + Backwards
    return is_palindrome(Sample[1:], Forwards, Backwards)
  else:
    return is_palindrome(Sample[1:], Forwards, Backwards)

