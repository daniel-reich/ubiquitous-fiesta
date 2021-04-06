
def asc_des_none(lst, s):
  d={'Asc':sorted(lst), 'Des':lst[::-1], 'None':lst[::]}
  return d[s]

