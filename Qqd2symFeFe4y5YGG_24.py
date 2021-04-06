
def palindromic_date(date):
  dates = date.split("/");
  return dates[0] == dates[1] and "".join(dates) == "".join(dates)[::-1];

