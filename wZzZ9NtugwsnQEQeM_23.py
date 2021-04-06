
def golf_score(par, scr):
  d = {'eagle':-2, 'birdie':-1, 'bogey':1, 'double-bogey':2, 'par':0}
  return sum(par[ind]+d[i] for ind, i in enumerate(scr))

