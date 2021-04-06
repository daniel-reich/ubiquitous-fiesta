
def pH_name(pH):
  if pH < 0 or pH > 14:
    return 'invalid'
  elif pH < 7:
    return 'acidic'
  elif pH > 7:
    return 'alkaline'
  elif pH == 7:
    return 'neutral'

