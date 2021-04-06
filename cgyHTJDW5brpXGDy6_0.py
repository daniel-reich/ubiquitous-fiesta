
from datetime import datetime as dt
def hours_passed(time1, time2):
    delta = (dt.strptime(time2, "%I:%M %p") -
             dt.strptime(time1, "%I:%M %p")).seconds // 3600
    return '{} hours'.format(delta) if delta else 'no time passed'

