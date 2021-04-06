
from datetime import datetime, timedelta
​
def current_streak(today, lst):
    x = 0
    lst3 = lst[::-1]
    if len(lst) == 0:
        return 0
    elif datetime.strptime(lst3[0]["date"], '%Y-%m-%d').date() == datetime.strptime(today, '%Y-%m-%d').date():
        for i, e in enumerate(lst3):
            if datetime.strptime(e["date"], '%Y-%m-%d').date() == datetime.strptime(today, '%Y-%m-%d').date():
                x = x+1
            elif datetime.strptime(e["date"], '%Y-%m-%d').date() == datetime.strptime(today, '%Y-%m-%d').date() - timedelta(days=i):
                x = x + 1
        return x
    else:
        return 0

