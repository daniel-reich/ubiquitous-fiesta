
def batting_avg(x):
  tot_h,tot_bats=0,0
  for a in x:
    hits,at_bat=a
    tot_h+=hits
    tot_bats+=at_bat
  return '{:.3f}'.format(tot_h/tot_bats)[1:]

