
def pH_name(pH):
  if(pH > 0 and pH < 14):
    if(pH < 7):
      return 'acidic'
    elif(pH > 8):
      return 'alkaline'
    else:
      return 'neutral'
  else:
    return 'invalid'

