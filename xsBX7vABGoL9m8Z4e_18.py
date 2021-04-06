
from datetime import datetime, timedelta
​
​
def fill(number, spaces):
  s = '%s' % number
  return s.zfill(spaces)
​
​
def sync_subs(subtitles, timeIncrement):
  try:
    offset = datetime.strptime(timeIncrement, '%H:%M:%S,%f')
  except Exception as e:
    print(e)
    return 'There is a problem with the second argument'
  else:
    offset = timedelta(hours=offset.hour, minutes=offset.minute,
                       seconds=offset.second, microseconds=offset.microsecond)
  lines = subtitles.split('\n')
  for i, line in enumerate(lines):
    line_text = []
    for j, word in enumerate(line.split(' ')):
      try:
        t = datetime.strptime(word, '%H:%M:%S,%f')
        t += offset
        hour = fill(t.hour, 2)
        minute = fill(t.minute, 2)
        second = fill(t.second, 2)
        millis = fill((t.microsecond // 1000), 3)
        s = '{}:{}:{},{}'.format(hour, minute, second, millis)
        line_text.append(s)
      except ValueError:
        line_text.append(word)
    lines[i] = ' '.join(line_text)
  txt = '\n'.join(lines)
  print(txt)
  return txt

