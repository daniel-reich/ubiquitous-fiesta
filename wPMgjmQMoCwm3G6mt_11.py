
def upload_count(dates, month):
    result = 0
    for i in dates:
        if month in i:
            result += 1
        else:
            continue
    return result

