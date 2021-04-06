
import functools
def time_sum(times):
  sum_fnc=lambda ttt:(lambda a:'%02d:%02d:%02d' % (divmod(divmod(a,60)[0],60)+(divmod(a,60)[1],)))((lambda a:functools.reduce(lambda x,y:x+y[0]*3600+y[1]*60+y[2],a,0))((lambda a:[list(map(int,i.split()[-1].split(':'))) for i in a])(ttt)))
  x = sum_fnc(times)
  new = x.split(":")
  return list(map(int, new))

