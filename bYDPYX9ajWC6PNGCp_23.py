
def track_robot(*s):
  return[sum(s[1::4])-sum(s[3::4]),sum(s[0::4])-sum(s[2::4])]

