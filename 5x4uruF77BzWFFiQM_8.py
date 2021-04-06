
def pH_name(pH):
  return 'alkaline' if pH > 7 and pH <= 14 else 'acidic' if pH < 7 and pH >= 0 else 'neutral' if pH == 7 else 'invalid'

