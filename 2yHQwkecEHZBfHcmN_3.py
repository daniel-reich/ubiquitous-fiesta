
def progress_days(runs):
    days = [j for i, j in enumerate(runs) if i != 0 and j > runs[i-1]]
    return len(days)

