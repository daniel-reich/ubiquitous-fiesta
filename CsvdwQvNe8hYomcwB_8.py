
def remap(value, low1, high1, low2, high2):
  if low1 == high1:
    return 0
  else:
    i = ((value-low1)*high2+low2*(high1-value))/(high1-low1)
    return round(i, 1)

