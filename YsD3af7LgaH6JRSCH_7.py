
import re
​
def time_adjust(now, hrs, mins, sec):
  hours_regex = re.compile(r"(\d\d):(\d\d):(\d\d)")
  hours,minutes,seconds =  [int(e) for e in re.findall(hours_regex , now)[0]];
  total_seconds  = (seconds +sec) +  (minutes+mins)*60 + (hours+hrs)*(60**2)
​
  result_hours  = str ( (total_seconds // 3600) %24 );
  result_minutes  = str( (total_seconds // 60) %60 );
  result_seconds  = str (total_seconds % 60 ); 
    
  return "{}:{}:{}".format(result_hours.zfill(2) , result_minutes.zfill(2) , result_seconds.zfill(2))

