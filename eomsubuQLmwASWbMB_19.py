
import datetime  
from datetime import date 
import calendar 
​
def weekday_dutch(date):
​
    
    def findDay(date): 
        day, month, year = (int(i) for i in date.split(' '))     
        born = datetime.date(year, month, day) 
        return born.strftime("%A") 
    
    dayd = {'Monday':'maandag','Tuesday':'dinsdag','Wednesday':'woensdag','Thursday':'donderdag','Friday':'vrijdag','Saturday':'zaterdag','Sunday':'zondag' }
    return(dayd[findDay(date)])

