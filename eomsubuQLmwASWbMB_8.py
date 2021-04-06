
import datetime 
import calendar
def weekday_dutch(date):
    obj = {"Monday":"maandag","Tuesday":"dinsdag","Wednesday":"woensdag","Thursday":"donderdag","Friday":"vrijdag",
"Saturday":"zaterdag","Sunday":"zondag" }
    return obj[calendar.day_name[datetime.datetime.strptime(date, '%d %m %Y').weekday()]]

