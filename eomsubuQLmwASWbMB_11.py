
from datetime import datetime
​
def weekday_dutch(date):
  day, month, year = map(int, date.split())
  return [
    "maandag",
        "dinsdag",
        "woensdag",
        "donderdag",
        "vrijdag",
        "zaterdag",
        "zondag",
    ][datetime(day=day, month=month, year=year).weekday()]

