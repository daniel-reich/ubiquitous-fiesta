
def longest_time(h, m, s):
  hrs, mins, secs = h*60*60, m*60, s
  return [h,m,s][([hrs,mins,secs]).index(max(hrs,mins,secs))]

