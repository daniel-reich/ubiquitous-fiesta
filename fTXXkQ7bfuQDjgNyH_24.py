
def day_of_year(date):
    dict= {1: 31 , 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    date = date.split('/')
    day=0
    for i in dict:
        if i==int(date[0]):
            break
        day+=dict[i]
    day+=int(date[1])
    if int(date[2])%100==0:
        if int(date[2])%400==0 and int(date[0])>2:
            return day+1
        else:
            return day
    else:
        if int(date[2])%4==0 and int(date[0])>2:
            return day+1
        else:
            return day

