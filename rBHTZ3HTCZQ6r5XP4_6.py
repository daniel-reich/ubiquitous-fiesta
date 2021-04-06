
def expanded_form(num):
  def get_parts(number, i=0):
    if i == len(number):
      return []
    else:
      tr = '1'
      while len(tr) < len(number[i:]):
        tr += '0'
      return [tr] + get_parts(number, i+1)
  def get_fractions(number, i=0):
    if i == len(number):
      return []
    else:
      if number[i] == '0':
        return [] + get_fractions(number, i+1)
      return ['{}/{}'.format(number[i], (10 ** (i+1)))] + get_fractions(number, i+1)
  
  num, dec = str(num).split('.')
  parts = get_parts(num)
  fracs = get_fractions(dec)
  
  prts = [str(int(num[n]) * int(parts[n])) for n in range(len(num)) if num[n] != '0'] + fracs
  
  return ' + '.join(prts)

