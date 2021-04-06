
def upload_count(dates, month):
    l = len(month)
    ctr = 0
    for i in dates:
        if i[:l] == month:
            ctr += 1
    return ctr

