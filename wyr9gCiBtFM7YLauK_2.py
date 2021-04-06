
def time_sum(times):
  timelist = [ x.split(":") for x in times ]
  seconds = sum([ int(x[2]) for x in timelist ])
  minutes = sum([ int(x[1]) for x in timelist ]) + int(seconds/60)
  hours = sum([ int(x[0]) for x in timelist ]) + int(minutes/60)
  
  return [ hours , minutes % 60 , seconds % 60]

