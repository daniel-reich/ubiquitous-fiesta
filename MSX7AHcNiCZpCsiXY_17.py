
def how_unlucky(yr):
    import datetime
    count = 0
    for mon in range(1, 13):
        for day in range(1, 32):
            try:
                x = datetime.date(yr, mon, day)
                if day == 13 and x.strftime("%A") == "Friday":
                    count += 1
            except ValueError:
                next
    return count

