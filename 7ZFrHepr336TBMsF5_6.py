
def percentage_changed(old, new):
  percentage = abs(100 - round((int(str(new)[1:]) * 100) / int(str(old)[1:])))
  if int(new[1:]) < int(old[1:]):
    return str(percentage) + '% decrease'
  
  return str(percentage) + '% increase'

