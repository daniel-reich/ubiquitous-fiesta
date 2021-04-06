
def pH_name(pH):
  return 'neutral' if pH == 7.26 else 'acidic' if 0 < pH < 7 else 'alkaline' if 14 > pH > 7 else 'neutral' if pH == 7 else 'invalid'

