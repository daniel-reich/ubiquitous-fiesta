
def format_phone_number(lst):
  pho_num = ''
  for i in range(10):
    if i == 0:
      pho_num = pho_num + '('
    elif i == 3:
      pho_num = pho_num + ') '
    elif i == 6:
      pho_num = pho_num + '-'
    pho_num = pho_num + str(lst[i])
  return pho_num

