
from datetime import datetime, timedelta
​
def current_streak(today, lst):
    dates = []
    for i in lst:
        dates.append(datetime.strptime(i['date'], '%Y-%m-%d'))
        if i['date'] == today:
            break
        
    today = datetime.strptime(today, '%Y-%m-%d')
    dates = dates[::-1]
    count = 1
    a = [1]
    for i in range(len(dates)-1):
        if dates[i+1] == dates[i] - timedelta(days=1):
            count += 1
            a.append(count)
        else:
            break
        
    return 0 if not lst or today not in dates else max(a)

