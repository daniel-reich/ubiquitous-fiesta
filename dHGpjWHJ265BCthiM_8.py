
from datetime import datetime, timedelta
​
​
def date_conversion(inp):
    return datetime(int(inp[0:4]), int(inp[5:7]), int(inp[8:]))
​
def current_streak(today, lst):
    if lst and lst[-1]['date'] == today:
        res = 1
        for d in range(len(lst) - 1, 0, -1):
            if date_conversion(lst[d]['date']) - date_conversion(lst[d-1]['date']) == timedelta(days=1):
                res+=1
            else:
                break
    else:
        return 0
    return res

