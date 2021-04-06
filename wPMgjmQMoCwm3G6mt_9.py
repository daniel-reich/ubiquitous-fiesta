
def upload_count(dates, month):
    return sum([i.count(month) for i in dates])

