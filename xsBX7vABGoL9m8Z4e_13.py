
import re
from datetime import datetime
from datetime import timedelta
def sync_subs(text,addtm): 
    try: 
        addtime = datetime.strptime(addtm, '%H:%M:%S,%f')
    except:
        return 'There is a problem with the second argument'
    delta = timedelta(hours = addtime.hour, minutes = addtime.minute, seconds = addtime.second, microseconds=addtime.microsecond)
    look1 = re.compile('[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9]')  
    start , newtext = 0 , '' 
    for match in re.finditer(look1,text): 
        try:
            time1 = datetime.strptime(match.group(), '%H:%M:%S,%f') 
            newtime = time1 + delta
            i,j = match.span()
            newtext = newtext + text[start:i] + newtime.strftime('%H:%M:%S,%f')[0:12]
            start = j
        except:
            continue
    return  newtext + text[start:(len(text) + 1)]

