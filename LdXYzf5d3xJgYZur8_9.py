
def longest_time(h, m, s):
  hm= h*60
  ms = s/60
  return h if hm > m and hm > ms else m if m > hm and m > ms else s

