
def century(year):
  cen = (year - 1)//100 + 1
  
  suffix = "th"
  if cen >= 20:
    lastDigit = cen%10
    if lastDigit == 1:
      suffix = "st"
    elif lastDigit == 2:
      suffix = "nd"
    elif lastDigit == 3:
      suffix = "rd"
  
  return str(cen) + suffix + " century"

