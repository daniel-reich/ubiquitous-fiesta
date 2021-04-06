
from datetime import datetime, timedelta
​
def add_n_days_to_a_date(date: str, n: int) -> str:
    day, month, year = int(date[:2]), int(date[2:4]), int(date[4:])
    end = datetime(year, month, day) + timedelta(days=n)
    return end.strftime('%d%m%Y')

