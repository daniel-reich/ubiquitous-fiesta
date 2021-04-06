
def upload_count(dates, month):
  return sum(1 if j.split(' ')[0] == month else 0 for j in dates)

