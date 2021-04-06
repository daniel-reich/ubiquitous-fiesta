
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
def countLeapYears(d):
        years = int(d[2])
        if (int(d[1]) <= 2):
            years -= 1
        return int(years / 4) - int(years / 100) + int(years / 400)
def days_between_dates(dt1, dt2):
        dt1=(int(dt1[0:2]),int(dt1[2:4]),int(dt1[4:]))
        dt2=(int(dt2[0:2]),int(dt2[2:4]),int(dt2[4:]))   
        n1 = dt1[2] * 365 + dt1[0]   
        for i in range(0, dt1[1] - 1):
            n1 += monthDays[i]
        n1 += countLeapYears(dt1)
        n2 = dt2[2] * 365 + dt2[0]
        for i in range(0, dt2[1] - 1):
            n2 += monthDays[i]
        n2 += countLeapYears(dt2)
        return abs(n2 - n1)

