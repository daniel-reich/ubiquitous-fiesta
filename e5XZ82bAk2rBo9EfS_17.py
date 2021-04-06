
from datetime import datetime as dt, timedelta as td
def bed_time(*times):
    return [dt.strftime(dt.strptime(t[0], '%H:%M')
                        - td(hours=dt.strptime(t[1], '%H:%M').hour,
                             minutes=dt.strptime(t[1], '%H:%M').minute),
                        '%H:%M')
            for t in times]

