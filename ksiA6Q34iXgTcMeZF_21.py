
def bonus(days):
  p33_40 = 325
  p41_48 = 550
  p49plus = 600
  
  if days < 33:
    total = 0
  elif days < 41:
    total = (days-32)*p33_40
  elif days < 49:
    total = (8*p33_40) + (days-40)*p41_48
  else:
    total = (8*p33_40) + (8*p41_48) + (days-48)*p49plus
  return total
"""
Days  Bonus
0 to 32 days  Zero
33 to 40 days SGD$325 per billable day
41 to 48 days SGD$550 per billable day
Greater than 48 days  SGD$600 per billable day
"""

