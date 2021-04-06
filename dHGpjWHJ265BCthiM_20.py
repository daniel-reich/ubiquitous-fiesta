
from datetime import datetime, timedelta
​
​
def make_date(date):
    year, month, day = map(int, date.split('-'))
    return datetime(year=year, month=month, day=day)
​
​
def current_streak(today, lst):
    if not lst or today != lst[-1]['date']:
        return 0
    dates = [make_date(i['date']) for i in lst[::-1]]
    delta = timedelta(days=-1)
    streak = 1
    for i, j in zip(dates, dates[1:]):
        if i + delta != j:
            break
        else:
            streak += 1
    return streak

