
import re, datetime  as dt
​
def sync_subs(subtitles, timeIncrement):
    if not re.search(r'\d\d(:[0-5]\d){2},\d{3}', timeIncrement): 
        return  'There is a problem with the second argument' 
    delta = dt.datetime.strptime(timeIncrement, '%H:%M:%S,%f')-dt.datetime(1900,1,1)
    
    def subs_function(match):
        moment = dt.datetime.strptime(match.group(), '%H:%M:%S,%f')
        return (moment+delta).strftime('%H:%M:%S,%f')[:-3]
        
    return re.sub(r'\d\d(:[0-5]\d){2},\d{3}', subs_function, subtitles)

