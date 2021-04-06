
def time_saved(s_lim, s_avg, d):
  T1=d/s_lim
  T2=d/s_avg
  Tmin=(T1-T2)*60
  return (round(Tmin,1))

