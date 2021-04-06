
def pH_name(pH):
  if pH > 0 and pH < 7: return 'acidic' 
  if pH >= 7 and pH < 8: return 'neutral'
  if pH > 7 and pH <= 14: return 'alkaline'
  return 'invalid'

