
def split_code(item):
  dg_tmp = ''
  alpha_tmp = ''
  for lt in item:
    if lt.isdigit():
      dg_tmp += lt
    elif lt.isalpha():
      alpha_tmp += lt
  return [alpha_tmp, int(dg_tmp)]

