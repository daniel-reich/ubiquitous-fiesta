
def lets_meet(distance, va, vb):
  time = distance / (va+vb)
  
  hours = str(int(time))
  minutes = str(int((time*60) % 60))
  seconds = str(int((time*3600) % 60))
  
  output = hours + "h " + minutes + "min " + seconds + "s"  
  return output

