
def pH_name(pH):
  if 0 <= pH <= 14:
    return 'acidic' if pH < 7 else 'alkaline' if pH > 7 else 'neutral'
  return 'invalid'

