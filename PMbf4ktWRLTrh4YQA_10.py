
months_31_days = [1,3,5,7,8,10,12];
def add_n_days_to_a_date(date, days):
    year = int(date[-4:]);
    month = int(date[2:4]);
    day = int(date[:2]);
    
    for i in range(days):
        day += 1;
        if(day == 32 and month == 12):
            day=1;
            month =1;
            year += 1;
        elif(month == 2):
            if((isLeapYear(year) == False and day == 29) or
                  (isLeapYear(year) and day == 30)):
                day =1;
                month += 1;
        elif((day == 31 and month not in months_31_days) or
            (day == 32 and month in months_31_days)):
            day = 1;
            month+=1;
       
    return str(day).zfill(2) + str(month).zfill(2) + str(year);
    
def isLeapYear(year):
    if(year % 4 == 0):
        if(year % 100 !=0 or year % 400 == 0):
            return True;
    return False;

