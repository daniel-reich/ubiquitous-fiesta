
def pH_name(pH):
  if pH<7 and pH>=0: return 'acidic'
  if pH == 7: return 'neutral'
  if pH >7 and pH<14: return 'alkaline'
  return 'invalid'

