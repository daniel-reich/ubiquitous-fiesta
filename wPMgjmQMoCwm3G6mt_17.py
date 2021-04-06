
def upload_count(dates, month):
  return [y for x in dates for y in x.split()].count(month)

