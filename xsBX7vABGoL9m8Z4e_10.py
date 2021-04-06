
def sync_subs(subtitles, timeIncrement):
  import re
  
  def parse(t):
    r = re.match(r"(\d+):(\d+):(\d+),(\d+)", t)
    if r is None:
      return None
    v = r.groups()
    for s in v[:3]:
      if not int(s) < 60:
        return None
    if not int(v[3]) < 1000:
      return None
    return float(v[0]) * 3600 + float(v[1]) * 60 + float(v[2]) + float(v[3]) * 0.001
  
  def make(i):
    return "{:0>2d}:{:0>2d}:{:0>2d},{:0>3d}".format(
      int(i // 3600), int(i % 3600 // 60), int(i % 60), int(i * 1000 % 1000))
  
  inc = parse(timeIncrement)
  if inc is None:
    return "There is a problem with the second argument"
  
  def repl(matchobj):
    v = matchobj.group(0)
    i = parse(v)
    i2 = i + inc
    return make(i2)
  
  return re.sub(r"\d+:\d+:\d+,\d+", repl, subtitles)

