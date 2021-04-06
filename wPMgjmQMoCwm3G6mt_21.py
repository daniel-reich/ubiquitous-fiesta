
def upload_count(dates, month):
  a = [i.split(" ")[0] for i in dates]
  return a.count(month)

