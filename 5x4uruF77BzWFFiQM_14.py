
def pH_name(ph):
  if ph < 7 and ph > 0:
    return 'acidic'
  elif ph > 7 and ph < 14:
    return 'alkaline'
  elif ph == 7:
    return 'neutral'
  else:
    return 'invalid'

