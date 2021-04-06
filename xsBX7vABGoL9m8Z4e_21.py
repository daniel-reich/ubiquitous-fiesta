
from datetime import datetime, timedelta
​
def sync_subs(subtitles, timeIncrement):
  pattern = '%H:%M:%S,%f'
  try:
    incr = datetime.strptime(timeIncrement, pattern)
  except:
    return "There is a problem with the second argument"
  incr = timedelta(hours=incr.hour, minutes=incr.minute, seconds=incr.second, milliseconds=incr.microsecond / 1000)
  lines = subtitles.splitlines()
  subs =  ['\n'.join(lines[i:i+3]) for i in range(0, len(lines), 3)]
  for i in range(len(subs)):
    parts = subs[i].splitlines()
    times = parts[1].split(' --> ')
    times = [datetime.strptime(t, pattern) + incr for t in times]
    times = [t.strftime(pattern)[:12] for t in times]
    parts[1] = ' --> '.join(times)
    subs[i] = '\n'.join(parts)
  return '\n'.join(subs)

