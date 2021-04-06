
def batting_avg(lst):
  return ('%.3f' % round(sum([i[0] for i in lst])/sum([i[1] for i in lst]),3))[1:]

