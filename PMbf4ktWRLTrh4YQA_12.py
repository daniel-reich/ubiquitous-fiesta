
def add_n_days_to_a_date(date, days):
    d = date[:2]
    m = date[2:4]
    y = date[4:]
    month = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
    if int(y) % 400 == 0 or (int(y) % 4 == 0 and int(y) % 100 != 0):
        month[1] = "29"
    for _ in range(0, days):
        if int(d) < int(month[int(m)-1]):
            d = str(int(d) + 1)
        elif int(m) < 12:
            m = str(int(m) + 1)
            d = "1"
        else:
            m = "1"
            d = "1"
            y = str(int(y) + 1)
            if int(y) % 400 == 0 or (int(y) % 4 == 0 and int(y) % 100 != 0):
                month[1] = 29
            else:
                month[1] = 28
    erg = "0" * (2 - len(d)) + d + "0" * (2 - len(m)) + m + "0" * (4 - len(y)) + y
    return erg

