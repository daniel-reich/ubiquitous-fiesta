
def upload_count(dates, month):
  l = [i for i in dates if month in i]
  return len(l)

