
import re
def sync_subs(subtitles, inc):
  times = re.findall(r"\d\d:\d\d:\d\d,\d\d\d",subtitles)
  tofill = re.sub(r"\d\d:\d\d:\d\d,\d\d\d","{}",subtitles)
  try: hi,mi,si,msi = [int(s) for s in inc.replace(",",":").split(":")]
  except: return "There is a problem with the second argument"
  if mi>=60: return "There is a problem with the second argument"
  def add(t1,t2):
    h1,m1,s1,ms1 = [int(s) for s in t1.replace(",",":").split(":")]
    h2,m2,s2,ms2 = [int(s) for s in t2.replace(",",":").split(":")]
    ms = ms1 + ms2
    s = s1 + s2 + ms//1000
    m = m1 + m2 + s//60
    h = h1 + h2 + m//60
    return "{:0>2}:{:0>2}:{:0>2},{:0>3}".format(h,m%60,s%60,ms%1000)
  return tofill.format(*[add(t,inc) for t in times])

