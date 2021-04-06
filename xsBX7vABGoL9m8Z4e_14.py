
import re
from datetime import datetime
def sync_subs(subtitles, timeIncrement):
  def helper(data):
    tmp=data.group(0)
    tp=datetime.strptime("30 Nov 00 "+tmp,"%d %b %y %H:%M:%S,%f")
    tp=(tp+add)
    return tp.strftime("%H:%M:%S,%f")[:-3]
  try:
    t0=datetime.strptime("30 Nov 00 "+"0:0:0,0","%d %b %y %H:%M:%S,%f")   
    tadd=datetime.strptime("30 Nov 00 "+timeIncrement,"%d %b %y %H:%M:%S,%f")
    add=(tadd-t0)
  except:
    return "There is a problem with the second argument"
​
  print(subtitles)
  new=re.sub('..:..:..,...', helper ,subtitles)
  print(new)
  return new

