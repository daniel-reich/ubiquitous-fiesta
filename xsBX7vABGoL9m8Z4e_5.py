
def sync_subs(subtitles, timeIncrement):
  import re
  try:
    h, m, s, ms = re.findall("(\d{2}):(\d{2}):(\d{2}),(\d{0,3})",timeIncrement)[0]
    h, m, s, ms = int(h), int(m), int(s), int(ms)
  except:
    m = 61
  if m >= 60 or s >= 60 or ms >= 1000:
    return "There is a problem with the second argument"
    
  for ts in re.findall("(\d{2}):(\d{2}):(\d{2}),(\d{3})",subtitles):
    repstr = "%s:%s:%s,%s" % ts
    nms = int(ts[3])+ms
    carry = 0
    if nms >= 1000:
      nms -= 1000
      carry = 1
    ns = int(ts[2])+s+carry
    if ns >= 60:
      ns -= 60
      carry = 1
    else: 
      carry = 0
    nm = int(ts[1])+m+carry
    if nm >= 60:
      nm -= 60
      carry = 1
    else: 
      carry = 0
    nh = int(ts[0])+h+carry
    subtitles = subtitles.replace(repstr,"%02d:%02d:%02d,%03d" % (nh, nm, ns, nms))
​
  return subtitles

