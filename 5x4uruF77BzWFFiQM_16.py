
def pH_name(pH):
  if pH > 0.0 and pH < 7.0:
    return "acidic"
  elif pH == 7.0:
    return "neutral"
  elif pH > 7.0 and pH <= 14.0:
    return "alkaline"
  else:
    return "invalid"

