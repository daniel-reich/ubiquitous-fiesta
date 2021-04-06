
def pH_name(pH):
  if pH < 0 or pH > 14:
    return('invalid')
  else:
    if pH == 7:
      return('neutral')
    elif pH < 7:
      return('acidic')
    else:
      return('alkaline')

