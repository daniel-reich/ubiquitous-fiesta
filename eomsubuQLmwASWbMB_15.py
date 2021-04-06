
def weekday_dutch(date):
    import datetime
    import calendar
    day, month, year = (int(i) for i in date.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    englishtodutch = {0: "maandag", 1: 'dinsdag', 2: 'woensdag', 3: 'donderdag', 4: 'vrijdag', 5: 'zaterdag', 6: 'zondag'}
    return(englishtodutch[dayNumber])

