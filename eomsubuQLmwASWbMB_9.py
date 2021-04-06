
import calendar
from datetime import datetime
​
dutch_days = {
  'monday': 'maandag', 'tuesday': 'dinsdag',
  'wednesday': 'woensdag', 'thursday': 'donderdag',
  'friday': 'vrijdag', 'saturday': 'zaterdag',
  'sunday': 'zondag'
}
​
def weekday_dutch(date):
  dt = datetime.strptime(date, "%d %m %Y").weekday()
  return dutch_days[calendar.day_name[dt].lower()]

