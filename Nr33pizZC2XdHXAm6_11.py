
from calendar import month_name
import datetime
​
def months_interval(dateStart, dateEnd):
    m_min = min(dateStart.month, dateEnd.month)
    m_max = max(dateStart.month, dateEnd.month)
    delta = ((dateEnd.year - dateStart.year),
             (dateEnd.month - dateStart.month))
    if delta[0] == 0:    
        return month_name[m_min:m_max+1] 
    elif abs(delta[0]) < 2 and delta[1] != 0:
        return [month_name[m_min]] + month_name[m_max:]
    else:
        return month_name[1:]

