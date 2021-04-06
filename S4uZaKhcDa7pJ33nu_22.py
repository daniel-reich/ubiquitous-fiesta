
from datetime import datetime, timedelta
def week_after(d):
  init = datetime.strptime(d,"%d/%m/%Y")
  final = init + timedelta(days = 7)
  return final.strftime("%d/%m/%Y")

