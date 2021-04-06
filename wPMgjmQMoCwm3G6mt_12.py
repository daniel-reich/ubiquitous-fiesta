
def upload_count(dates, month):
  count = 0
  for x in dates:
    y = x.split(' ')
    if y[0] == month:
      count += 1
  return count

