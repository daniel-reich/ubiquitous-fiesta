
def convert(n):
  return  '{}*F'.format(round(int(n.split('*')[0])*1.8+32)) if 'C' in n else '{}*C'.format(round((int(n.split('*')[0])-32)/1.8)) if 'F' in n else 'Error'

