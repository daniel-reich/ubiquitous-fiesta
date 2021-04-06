
def progress_days(runs):
    return len([y for x,y in enumerate(runs[1:]) if runs[x+1] > runs[x]])

