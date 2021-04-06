
def longest_time(h, m, s):
  return [h, m, s][[h*3600, m*60, s].index(max([h*3600, m*60, s]))]

