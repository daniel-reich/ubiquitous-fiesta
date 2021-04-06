
def return_end_of_number(num):
  ord = 'TH'
  num = str(num)
  
  if num[-1] == '1' and num[-2:] != '11': ord = 'ST'
  if num[-1] == '2' and num[-2:] != '12': ord = 'ND'
  if num[-1] == '3' and num[-2:] != '13': ord = 'RD'
  
  
  return '{}-{}'.format(num, ord)

