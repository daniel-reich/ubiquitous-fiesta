
def is_apocalyptic(n):
  L=str(2**n).split('666')
  if len(L)==1:
    return "Safe"
  elif len(L)==2:
    return "Single"
  elif len(L)==3:
    return "Double"
  elif len(L)==4:
    return "Triple"

