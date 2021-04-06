
def time_adjust(now, hrs, mins, sec):
  h, m, s = map(int,now.split(':'))
  s+=sec ; m+=mins+s//60 ; h+=hrs+m//60
  return '{:02d}:{:02d}:{:02d}'.format(h%24, m%60, s%60)

