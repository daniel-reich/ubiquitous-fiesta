
from datetime import datetime, timedelta
​
​
def week_after(date: str) -> str:
    in_week = datetime.strptime(date, '%d/%m/%Y') + timedelta(days=7)
    return in_week.strftime("%d/%m/%Y")

