
def add_n_days_to_a_date(date, days):
    dpm = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    d, m, y = int(date[:2]), int(date[2:4]), int(date[4:])
    dpm[2] += (y % 4 == 0)-(int(str(y)[-1:-3:-1]) == 0)*((y//100 % 4)>0)
    while days > dpm[m] - d:
        if not m:
            y += 1
            dpm[2] = 28+(y%4==0)-(int(str(y)[-1:-3:-1])==0)*((y//100 % 4)>0)
        days, m, d  = days-(dpm[m]-d+1), (m + 1) % 12, 1
    if not m: m = 12
    return format(d+days,'02d')+format(m,'02d')+str(y)

