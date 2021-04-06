
def progress_days(runs):
    return len([runs[i] for i in range(1,len(runs)) if runs[i-1]<runs[i]])

