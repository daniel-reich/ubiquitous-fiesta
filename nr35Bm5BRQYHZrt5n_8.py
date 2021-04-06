
def upward_trend(lst):
  x=0
  try:
    x=sum(lst)
  except:
    return "Strings not permitted!"
  else:
    if(lst==sorted(lst)):
      return True
    else:
      return False

