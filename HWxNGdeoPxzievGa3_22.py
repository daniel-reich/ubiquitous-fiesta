
def is_strange_pair(f, s):
  try:
    return True if (f,s)==('','') else f[0]==s[-1] and f[-1]==s[0] 
  except:
    return False

