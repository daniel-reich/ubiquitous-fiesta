
def flip_list(lst):
  if not lst:
    return []
    
  if any(isinstance(i, list) for i in lst):
    return [i for sub in lst for i in sub]
  else:
    return [[i] for i in lst]

