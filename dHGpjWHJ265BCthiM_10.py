
def current_streak(today, lst):
    streak = 0
    ty, tm, td = today.split("-")
    if not lst:
        return 0
    while {"date" : "{}-{}-{}".format(ty, tm, int(td) - streak)} in lst:
        streak += 1
    return streak

