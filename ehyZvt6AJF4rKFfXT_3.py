
def uncensor(s, V):
  return s.replace('*', '%s') % tuple(V)

