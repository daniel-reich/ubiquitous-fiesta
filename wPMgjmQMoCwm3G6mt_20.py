
def upload_count(dates, month):
  return sum(d.startswith(month) for d in dates)

