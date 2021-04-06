
def convert(deg):
​
    try:
      temp, unit = deg.split('*')
    except:
      return 'Error'
    
    if unit == 'F':
      return str(round((int(temp) - 32) / 1.8)) + '*' + 'C'
      
    if unit == 'C':
      return str(round((int(temp) * 1.8) + 32)) + '*' + 'F'

