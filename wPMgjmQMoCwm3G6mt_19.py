
def upload_count(dates, month):
    uploads = 0
    
    for count in dates:
        if month in count:
            uploads+=1
    return uploads

