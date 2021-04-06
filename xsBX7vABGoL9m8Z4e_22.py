
import re
def sync_subs(subtitles, timeIncrement):
  if not re.match(r'([0-9]{2}:[0-5][0-9]:[0-5][0-9],[0-9]{3})', timeIncrement): return "There is a problem with the second argument"
  
  def to_ms(t):
    h, m, s, ms = [int(i) for i in t.replace(",",":").split(":")]
    return sum([h*3600000, m*60000, s*1000, ms])
  def to_str(t):
    ms = t%1000
    t //= 1000
    s = t%60
    t //= 60
    m = t%60
    t //= 60
    h = t
    return "{}:{}:{},{}".format(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2), str(ms).zfill(3))
  timeIncrement = to_ms(timeIncrement)
  o = []
  for ts in re.findall(r'([0-9]{2}:[0-5][0-9]:[0-5][0-9],[0-9]{3})', subtitles):
    o.append(to_str(to_ms(ts)+timeIncrement))
  subtitles = re.sub(r'([0-9]{2}:[0-5][0-9]:[0-5][0-9],[0-9]{3})', '{}', subtitles)
  return subtitles.format(*o)

