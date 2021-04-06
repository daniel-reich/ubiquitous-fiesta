
import datetime
​
​
def current_streak(today, lst):
    streak = 0
    all_dates = []
    today = tuple(map(int, today.split("-")))
    today = datetime.date(today[0], today[1], today[2])
​
    for i in range(len(lst)):
        for k, v in lst[i].items():
            cur_date = tuple(map(int, v.split("-")))
            cur_date = datetime.date(cur_date[0], cur_date[1], cur_date[2])
            all_dates.append(cur_date)
    if not all_dates:
        return 0
    if all_dates[-1].day == today.day:
        streak += 1
        for y in range(2, len(all_dates) + 1):
            if all_dates[-y].day == today.day - y + 1:
                streak += 1
    print(streak)
    return streak

