
def current_streak(today, lst):
    count = 1
    if not lst:
        return 0
    if lst[-1]['date'] != today:
        return 0
    for day in range(len(lst) - 1):
        if int(lst[day]['date'][-2:]) + 1 == int(lst[day+1]['date'][-2:]):
            count += 1
        else:
            count = 1
    return count

