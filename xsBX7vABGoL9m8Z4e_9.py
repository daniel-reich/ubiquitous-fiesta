
from datetime import datetime, timedelta
import re
​
units=['hours', 'minutes', 'seconds', 'milliseconds']
​
​
def sync_subs(subtitles, timeIncrement):
    times = re.finditer('([0-9]{2}:){2}[0-9]{2},[0-9]{3}', subtitles)
    for time in times:
        dt_time = datetime.strptime (time.group(), '%H:%M:%S,%f')
        if not re.match ('([0-5][0-9]:){2}[0-9]{2},[0-9]{3}',timeIncrement):
            return 'There is a problem with the second argument'
        change = timedelta(**dict(zip(units, map(int, re.findall('[0-9]+', timeIncrement)))))
        dt_time += change
        subtitles= subtitles.replace(time.group(), dt_time.strftime('%H:%M:%S,%f')[:-3])
​
    return subtitles

