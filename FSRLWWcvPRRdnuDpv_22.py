
class time:
  def __init__(self, hour, minute):
    self.hour = hour
    self.minute = minute
    
  def time_till(current, target):
    if target.hour > current.hour or target.hour == current.hour and target.minute > current.minute:
      if target.minute >= current.minute:
        return [target.hour - current.hour, target.minute - current.minute]
      else:
        return [target.hour - current.hour - 1, target.minute+60 - current.minute]
    if target.hour < current.hour or target.hour == current.hour and target.minute < current.minute:
      if current.minute == 0:
        return [24 - current.hour + target.hour, current.minute]
      else:
        return [24 - current.hour + target.hour - 1, abs(current.minute - 60)]
    return [0, 0]
    
def time_to_eat(current_time):
  if current_time.index(':') == 2:
    hours = int(current_time[0:2])
    minutes = int(current_time[3:5])
  else:
    hours = int(current_time[0])
    minutes = int(current_time[2:4])
  if current_time[5] == 'p' or current_time[6] == 'p':
    hours += 12
  if current_time[0:2] == '12' and current_time[6] == 'a':
    hours = 0
    
  now = time(hours, minutes)
  breakfast = time(7, 0)
  lunch =  time(12, 0)
  dinner = time(19, 0)
  
  time_to_dinner = time.time_till(now, dinner)
  time_to_lunch =  time.time_till(now, lunch)
  time_to_breakfast = time.time_till(now, breakfast)
  
  if time_to_dinner[0] < time_to_lunch[0] and time_to_dinner[0] < time_to_breakfast[0]:
    return time.time_till(now, dinner)
  if time_to_lunch[0] < time_to_dinner[0] and time_to_lunch[0] < time_to_breakfast[0]:
    return time.time_till(now, lunch)
  return time.time_till(now, breakfast)

