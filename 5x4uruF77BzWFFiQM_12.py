
def pH_name(pH):
  return 'acidic' if int(pH) >= 0 and int(pH) < 7 else 'neutral' if int(pH) == 7 else 'alkaline' if int(pH) >= 8 and int(pH) < 14 else 'invalid'

