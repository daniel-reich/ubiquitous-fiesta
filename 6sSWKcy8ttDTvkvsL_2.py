
def afterNdays(days, n):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return [week[(week.index(d)+n)%7] for d in days]

