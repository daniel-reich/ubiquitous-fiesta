
import datetime
def months_interval(dateStart, dateEnd):
    dateStart,dateEnd = min(dateStart,dateEnd),max(dateStart,dateEnd)
    
    month_list = []
    d = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    
    year_diff = dateEnd.year - dateStart.year
    month_diff = dateEnd.month - dateStart.month
    
    total_month_diff = (year_diff*12)+month_diff
    
    if total_month_diff > 11:
        month_list = list(d.values())
    else:
        for month in range(dateStart.month,dateStart.month+total_month_diff+1):
            mcopy = month
            if mcopy > 12:
                mcopy -= 12
            month_list.append(d[mcopy])
            
    return [i for i in list(d.values()) if i in month_list]

