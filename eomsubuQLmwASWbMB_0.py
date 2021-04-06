
from time import strptime
dutch_days = ['maandag', 'dinsdag', 'woensdag', 'donderdag',
              'vrijdag', 'zaterdag', 'zondag']
def weekday_dutch(date):
    return dutch_days[strptime(date, '%d %m %Y').tm_wday]

