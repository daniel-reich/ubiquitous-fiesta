
def weekday_dutch(date):
    import datetime
    list1=date.split(' ')
    day1=datetime.date(int(list1[2]),int(list1[1]),int(list1[0])).isoweekday()
    if day1 == 1:
        return 'maandag'
    elif day1 == 2:
        return 'dinsdag'
    elif day1 == 3:
        return 'woensdag'
    elif day1 == 4:
        return 'donderdag'
    elif day1 == 5:
        return 'vrijdag'
    elif day1 == 6:
        return 'zaterdag'
    elif day1 == 7:
        return 'zondag'

