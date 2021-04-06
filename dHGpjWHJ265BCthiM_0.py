
from datetime import datetime as dt
​
def current_streak(today, lst):
    today = dt.strptime(today, '%Y-%m-%d')
    dates = [dt.strptime(i['date'], '%Y-%m-%d') for i in lst]
    
    if not dates or today not in dates:
        return 0
    
    streak = 1
    pos = dates.index(today)
    while (dates[pos] - dates[pos-1]).days == 1:
        streak += 1
        pos -= 1
    return streak

