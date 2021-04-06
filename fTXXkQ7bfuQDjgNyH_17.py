
def day_of_year(date):
    year_dct = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
                10: 31, 11: 30, 12: 31}
​
    date_split = date.split("/")
    month = date_split[0]
    day = date_split[1]
    year = date_split[-1]
    if ((int(year) % 100 == 0 and int(year) % 400 == 0) or (int(year) % 100 != 0 and int(year) % 4 == 0)) and int(month) > 2:
        return sum(year_dct[month] for month in range(1, int(month))) + int(day) + 1
    else:
         return sum(year_dct[month] for month in range(1, int(month))) + int(day)

