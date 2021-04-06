
def lets_meet(distance, va, vb):
  time_in_hrs = distance / (va + vb)
  time_in_sec = time_in_hrs * 60 * 60
  
  seconds = time_in_sec % 60
  minutes = (time_in_sec // 60)  % 60
  hours = (time_in_sec // 60) // 60
  
  return "{}h {}min {}s".format(int(hours), int(minutes), int(seconds))

