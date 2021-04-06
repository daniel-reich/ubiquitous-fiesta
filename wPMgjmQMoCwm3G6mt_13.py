
def upload_count(dates, month):
  return len([date for date in dates if date.split()[0]==month])

