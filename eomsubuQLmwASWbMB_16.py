
import datetime
def weekday_dutch(datein):
    dow = {0:'maandag',
           1:'dinsdag',
           2:'woensdag',
           3:'donderdag',
           4:'vrijdag',
           5:'zaterdag',
           6:'zondag',}
    d, m, y = datein.split()
    dt = datetime.datetime(int(y), int(m), int(d))
    return dow[dt.weekday()]

