
import datetime
def weekday_dutch(d):
  w=["zondag","maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag"]
  return w[int(datetime.datetime(*list(map(int,d.split()))[::-1]).strftime('%w'))]

