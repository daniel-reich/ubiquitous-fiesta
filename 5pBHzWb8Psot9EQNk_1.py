
def simple_encoder(s):
  lst=s.lower()
  single=""
  double=""
  for e in list(lst):
    if e in single:
      double+=e
    else:
      single+=e
  result=""
  for e in list(lst):
    if e in double:
      result+="]"
    else:
      result+="["
  return(result)

