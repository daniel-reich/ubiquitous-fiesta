
def daily_streak(lst):
    count = 0
    streaks = []
    for i in range(len(lst)):
        if lst[i]:
            count+=1
        else:
            count = 0
        streaks.append(count)
    return(max(streaks))

