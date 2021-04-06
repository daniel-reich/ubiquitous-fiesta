
def is_truthy(val):
  validation = bool(val)
  
  if validation == False or None or 0 or "" or {} or []:
    return 0
  else:
    return 1

