
def convert(d):
  temp = '';
  if d.find('C') != -1:
    temp = "{}*F".format(round(1.8000 * int(d[0:d.index('C')-1]) + 32));
  elif d.find('F') != -1:
    temp = "{}*C".format(round((int(d[0:d.index('F')-1]) - 32)/1.8));
  else:
    temp = 'Error'
  return temp;

