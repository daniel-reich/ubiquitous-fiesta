
def expanded_form(num):
  def get_parts(number, i=0):
    if i == len(number):
      return []
    else:
      tr = '1'
      while len(tr) < len(number[i:]):
        tr += '0'
      return [tr] + get_parts(number, i+1)
      
  num = str(num)
  parts = get_parts(num)
  
  prts = [str(int(num[n]) * int(parts[n])) for n in range(len(num)) if num[n] != '0']
  
  return ' + '.join(prts)

