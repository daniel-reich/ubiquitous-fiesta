
def current_streak(today, lst):
    streak = 0
    days = list(map(lambda x: x["date"], lst))
    if days and days[-1] == today:
        streak = 1
        for i in range(1, len(days)):
            gap = int(days[-i][-2:]) - int(days[-i-1][-2:])
            if gap != 1:
                break
            streak += 1
    return streak

