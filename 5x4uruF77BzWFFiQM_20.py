
def pH_name(pH):
  return 'invalid' if pH < 0 or pH > 14 else 'acidic' if pH < 7 else 'alkaline' if pH >7 else 'neutral'

