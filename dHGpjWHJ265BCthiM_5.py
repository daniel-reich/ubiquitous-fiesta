
def current_streak(today, lst):
    if len(lst)==0:
        return 0
    month = int(today[5:7])
    arr = [int(x['date'][-2:]) for x in lst if int(x['date'][5:7]) == month]
​
    today = int(today[-2:])
​
    if today - arr[-1] > 1:
        return 0
    
    else:
        for i in range(today-1, 1, -1):
            if i not in arr:
                return today - i

