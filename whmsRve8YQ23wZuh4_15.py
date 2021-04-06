
from datetime import datetime
def sort_dates(lst, mode):
  return [e.strftime("%d-%m-%Y_%H:%M") for e in sorted([datetime.strptime(f, '%d-%m-%Y_%H:%M') for f in lst], reverse=(mode != "ASC"))]

