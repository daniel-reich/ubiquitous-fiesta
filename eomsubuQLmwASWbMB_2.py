
import datetime 
import calendar 
def weekday_dutch(date):
    translate = {'Monday':'maandag','Wednesday':'woensdag','Thursday':'donderdag','Tuesday':'dinsdag','Friday':'vrijdag','Saturday':'zaterdag','Sunday':'zondag'}
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return translate[calendar.day_name[born]]

