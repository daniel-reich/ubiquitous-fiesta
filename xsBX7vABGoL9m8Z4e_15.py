
from datetime import datetime, timedelta
import re
​
​
def sync_subs(subtitles, timeIncrement):
    timeFormat = "%H:%M:%S,%f"
    try:
        tmp = datetime.strptime(timeIncrement, timeFormat)
        deltaTime = timedelta(hours=tmp.hour, minutes=tmp.minute,
                              seconds=tmp.second, microseconds=tmp.microsecond)
    except ValueError:
        return "There is a problem with the second argument"
​
    def fixtime(x):
        return datetime.strftime((datetime.strptime(x, timeFormat) + deltaTime),
                                 timeFormat)[:-3]
​
    return re.sub(r"\d{2}:\d{2}:\d{2}\,\d{3}", lambda x: fixtime(x.group()),
                  subtitles)

