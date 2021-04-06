
def reversible_inclusive_list(start, end):
  if start == end : 
    return [end] 
  else: 
    return [start] + reversible_inclusive_list(start+int((end-start)/abs(end-start)), end) if start != end else [end]

