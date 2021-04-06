
def upload_count(dates, month):
  return sum(date.startswith(month) for date in dates)

