
def pH_name(pH):
  if pH >= 0.00 and pH < 6.99:
    return "acidic"
  elif pH >= 7.00 and pH <= 7.99:
    return "neutral"
  elif pH >= 8.00 and pH <= 14.00:
    return "alkaline"
  else:
    return "invalid"
  
  
  #Given a pH value, return whether that value is "alkaline", "acidic", or "neutral". 
  #Return "invalid" if the value given is less than 0 or greater than 14.

