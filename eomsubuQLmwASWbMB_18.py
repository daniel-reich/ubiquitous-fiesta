
import datetime
import calendar
def weekday_dutch(date):
    days = {"Monday":"maandag" ,
            "Sunday":"zondag" ,
            "Tuesday":"dinsdag" ,
            "Wednesday":"woensdag",
            "Thursday":"donderdag" ,
            "Friday":"vrijdag",
            "Saturday":"zaterdag"}
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    for i,j in days.items():
        if calendar.day_name[born] == i:
            return (j)

