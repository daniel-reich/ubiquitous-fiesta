
def daily_streak(lst):
    streak, runs = 0, [0]
    for day in lst:
        if day:
            streak += 1
        else:
            runs.append(streak) 
            streak = 0
    runs.append(streak)
    return max(runs)

