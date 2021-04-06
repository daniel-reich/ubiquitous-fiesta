
def is_pandigital(n):
  number=str(n)
  sets=set([item for item in number])
  if(len(sets)!=10):
    return False
  else:
    return True

