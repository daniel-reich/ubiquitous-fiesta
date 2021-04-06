
def convert(deg):
  try:
    t,c = deg.split('*')
    return str(round(int(t) * 9/5 + 32)) + '*F' if c=='C' else str(round((int(t) - 32) * 5/9)) + '*C'
  except:
    return "Error"

