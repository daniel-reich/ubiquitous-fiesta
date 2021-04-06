
def asc_des_none(lst, s):
  return lst if s == 'None' else sorted(lst, reverse=(s=='Des'))

