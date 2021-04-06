
def time_adjust(now, hrs, mins, sec):
  t = now.split(":")
  h = int(t[0])
  m = int(t[1])
  s = int(t[2])
  if sec>=60:
    mins += sec//60
    sec=sec%60
  if mins>=60:
    hrs += mins//60
    mins=mins%60
  if hrs>=24:
    hrs = hrs%24
  H = h+hrs
  M = m+mins
  S = s+sec
  if S>=60:
    M += S//60
    S=S%60
  if M>=60:
    H += M//60
    M=M%60
  if H>=24:
    H = H%24
  return "%02d"%(H,)+":"+"%02d"%(M,)+":"+"%02d"%(S,)

