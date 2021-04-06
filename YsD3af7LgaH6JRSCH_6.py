
def time_adjust(now, hrs, mins, sec):
  now_time = list(map(int, now.split(':')))
  now_time = [now_time[0] + hrs, now_time[1] + mins, now_time[2] + sec]
  hrs_now, mins_now, sec_now = now_time[0], now_time[1], now_time[2]
  if sec_now - 60 >= 0:
    mins_now += sec_now // 60
    sec_now = sec_now % 60
  else:
    sec_now = sec_now
  if mins_now - 60 >= 0:
    hrs_now += mins_now // 60
    mins_now = mins_now % 60
  else:
    mins_now = mins_now
  if hrs_now - 24 >= 0:
    hrs_now = hrs_now % 24
  else:
    hrs_now = hrs_now
  return '{:02d}:{:02d}:{:02d}'.format(hrs_now, mins_now, sec_now)

