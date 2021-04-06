
def dolla_dolla_bills(money):
  def format_dollars(dollars):
    commas = []
  
    n = -1
    s = ''
    m = dollars.replace('-','')
  
    while abs(n) <= len(m):
      if len(s) == 3:
        commas.append(''.join(list(reversed(s))))
        s = ''
    
      s += m[n]
      n -= 1
    
    if s != '':
      commas.append(''.join(list(reversed(s))))
    
    if '-' in dollars:
      sign = '-'
    else:
      sign = ''
      
    return '{}$'.format(sign) + ','.join(list(reversed(commas)))
  def format_cents(cents):
    
    print(cents)
    if len(cents) < 2:
      while len(cents) < 2:
        cents += '0'
    elif len(cents) > 2:
      cents = str(round(float('0.' + cents),2))[2:]
    print(cents)
    return cents
  
  
  money = str(money)
  if '.' in money:
    dollars, cents = money.split('.')
  else:
    dollars, cents = [money, '0']
  
  fd = format_dollars(dollars)
  fc = format_cents(cents)
  
  return fd + '.' + fc

