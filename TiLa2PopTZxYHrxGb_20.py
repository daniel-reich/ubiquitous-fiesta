
def playback_duration(duration, speed):
  if speed==1: return duration
  duration=duration.split(':')
  a=((int(duration[0])*3600)+(int(duration[1])*60)+int(duration[2]))/speed
  duration[0]=int(a//3600)
  duration[1]=int((a-(duration[0]*3600))//60)
  duration[2]=int(a-((duration[0]*3600)+(duration[1]*60)))
  return ':'.join([str(i).zfill(2) for i in duration])

