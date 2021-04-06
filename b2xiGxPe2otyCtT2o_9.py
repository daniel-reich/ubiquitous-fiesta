
def how_many_times(n):
  if len(n)==0:
    return 0
  else:
    return ('abcdefghijklmnopqrstuvwxyz'.index(n[-1])+1)+how_many_times(n[0:-1])

