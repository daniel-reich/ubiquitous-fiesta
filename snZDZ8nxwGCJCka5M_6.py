
def pyramidal_string(string, _type):
  n = 1/2 * ((8 * len(string) + 1)**(1/2) - 1)
  if not n.is_integer():
    return 'Error!'
  start, end, step = (1, int(n)+1, 1) if _type == 'REG' else (int(n), 0, -1)
  s = list(string)
  pyr = []
  for i in range(start, end, step):
    bloc = []
    for j in range(i):
      bloc.append(s.pop(0))
    pyr.append(' '.join(bloc))
  return pyr

