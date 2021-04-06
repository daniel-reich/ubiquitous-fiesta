
def format_date(date):
  date_list = date.split("/")
  date_list.reverse()
  date = ""
  for i in date_list:
    date += i
  return date

