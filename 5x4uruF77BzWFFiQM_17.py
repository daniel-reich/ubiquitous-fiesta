
def pH_name(pH):
  if pH < 0 or pH > 14:
    return 'invalid'
  if pH < 7:
    return 'acidic'
  elif pH == 7:
    return 'neutral'
  elif pH > 7:
    return 'alkaline'
