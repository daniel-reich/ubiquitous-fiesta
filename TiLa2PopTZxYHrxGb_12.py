
def playback_duration(duration, speed):
  A=duration.split(':')
  ts=int((int(A[0])*3600+int(A[1])*60+int(A[2]))/speed)
  h,r1=divmod(ts, 3600)
  m,s=divmod(r1, 60)
  H=str(h).zfill(2) if h<100 else str(h)
  M=str(m).zfill(2)
  S=str(s).zfill(2)
  return '{}:{}:{}'.format(H,M,S)

