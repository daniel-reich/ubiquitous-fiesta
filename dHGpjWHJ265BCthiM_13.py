
import datetime
​
def current_streak(today, lst):
    if len(lst) == 0:
        return 0
    t = datetime.datetime.strptime(today, '%Y-%m-%d')
    t = int(t.strftime('%j'))
​
    d = []
    for i in range(len(lst)):
        x = lst[i]['date']
        temp = datetime.datetime.strptime(x, '%Y-%m-%d')
        d.append(int(temp.strftime('%j')))
​
    if d[-1] != t:
        return 0
​
    for i in range(len(d)-1,-1,-1):
        if d[i] - d[i-1] != 1:
            return t-d[i]+1

