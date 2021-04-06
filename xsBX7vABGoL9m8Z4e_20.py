
import re
def sync_subs(subtitles, timeIncrement):
  if '60' in timeIncrement or not re.match('\d{2}\:\d{2}\:\d{2}\,\d{3}',timeIncrement):
    return 'There is a problem with the second argument'
​
  timeIncrement = [int(i) for i in re.findall('\d+',timeIncrement)]
  if subtitles.count('-->') == 1:
    return align_subtitles(subtitles, timeIncrement)
  else:
    subtitles = subtitles.split('\n')
    subtitles1 = align_subtitles('\n'.join(subtitles[:3]),timeIncrement)
    subtitles2 = align_subtitles('\n'.join(subtitles[3:]),timeIncrement)
    return '\n'.join([subtitles1,subtitles2])
​
def align_subtitles(subtitles, timeIncrement):
  stamp = subtitles[:3]
  arrow = '-->'
  text = subtitles[34:]
​
  time1, time2 = get_times(subtitles)
  time1_up = build_time_string(inc_time(time1,timeIncrement))
  time2_up = build_time_string(inc_time(time2,timeIncrement))
  final_time_string = ' '.join([time1_up, arrow, time2_up])
​
  return '\n'.join([stamp, final_time_string, text])
​
def get_times(txt):
  time1, time2 = re.findall('\d{2}\:\d{2}\:\d{2}\,\d{3}',txt)
  time1 = [int(i) for i in re.findall('\d+',time1)]
  time2 = [int(i) for i in re.findall('\d+',time2)]
  return time1, time2
​
def inc_time(time,inc):
  val = [60,60,1000]
  for i in range(0,-4,-1):
    time[i] += inc[i]
    if time[i] > val[i]:
      time[i] -= val[i]
      time[i-1] += 1
  return time
​
def build_time_string(time):
  h, m, s, ms = time
  return '%02d:%02d:%02d,%03d' % (h, m, s, ms)

