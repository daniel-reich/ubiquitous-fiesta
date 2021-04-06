
class Time:
  
  def get_seconds(time):
    hours, mins, secs = [int(i) for i in time.split(':')]
    secs += int(hours * 3600)
    secs += int(mins * 60)
    
    return secs
  
  def update_time_speed(seconds, speed_rate):
    return seconds // speed_rate
  
  def get_hours_mins_secs(seconds):
    hours = str(int(seconds // 3600))
    seconds = seconds % 3600
    mins = str(int(seconds // 60))
    seconds = str(int(seconds % 60))
    
    while len(hours) < 2:
      hours = '0' + hours
    while len(mins) < 2:
      mins = '0' + mins
    while len(seconds) < 2:
      seconds = '0' + seconds
    
    return ':'.join([hours, mins, seconds])
​
def playback_duration(duration, speed):
  
  seconds = Time.get_seconds(duration)
  updated = Time.update_time_speed(seconds, speed)
  print(seconds, updated)
  return Time.get_hours_mins_secs(updated)

