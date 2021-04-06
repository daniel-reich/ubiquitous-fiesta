
def upload_count(dates, month):
  return len(list(filter(lambda x:x.count(month)==1,dates)))

