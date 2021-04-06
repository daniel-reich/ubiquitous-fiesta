
def time_difference(city_a, timestamp, city_b):
    import calendar
    city_dic = {'Los Angeles': '-08:00', 'New York': '-05:00', 'Caracas': '-04:30',
                'Buenos Aires': '-03:00', 'London': '00:00', 'Rome': '01:00', 'Moscow': '03:00',
                'Tehran': '03:30', 'New Delhi': '05:30', 'Beijing': '08:00', 'Canberra': '10:00'}
    month_dic = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May':5,
                 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
                 'November': 11, 'December':12}
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    a_zone = city_dic[city_a]
    b_zone = city_dic[city_b]
    a_time = a_zone.split(':')
    b_time = b_zone.split(':')
    time_list = timestamp.split(' ')
    month = month_dic[time_list[0]]
    date_temp = []
    for i in range(2):
        if time_list[1][i] in numbers:
            date_temp.append(time_list[1][i])
    date = int(''.join(date_temp))
    year = int(time_list[2])
    time = time_list[3].split(':')
​
    if int(a_time[0])<=0 and int(b_time[0])>=0:
        time[0] = int(time[0])+(abs(int(a_time[0]))+int(b_time[0]))
    elif int(a_time[0])>=0 and int(b_time[0])<=0:
        time[0] = int(time[0])-(int(a_time[0])-int(b_time[0]))
    elif int(a_time[i])<int(b_time[i]):
        time[0] = int(time[0])+(int(b_time[0])-int(a_time[0]))
    else:
        time[0] = int(time[0])+(int(a_time[0])-int(b_time[0]))
​
    if int(a_time[1])<int(b_time[1]) and int(b_time[0])>0:
        time[1] = int(time[1])+(int(b_time[1])-int(a_time[1]))
    elif int(a_time[1])<int(b_time[1]) and int(b_time[0])<0:
        time[1] = int(time[1])-(int(b_time[1])-int(a_time[1]))
    elif int(a_time[1])>int(b_time[1]) and int(b_time[0])>0:
        time[1] = int(time[1])-(int(a_time[1])-int(b_time[1]))
    else:
        time[1] = int(time[1])+(int(a_time[1])-int(b_time[1]))
        
    for i in range(len(time)):
        if type(time[i]) is not int:
            time[i] = int(time[i])
            
    if time[1] >=60:
        time[0] += 1
        time[1] -= 60
    elif time[1] <0:
        time[0] -= 1
        time[1] += 60
    if time[0] >=24:
        date += 1
        time[0] -= 24
    elif time[0] <0:
        date -= 1
        time[0] += 24
​
    month_range = calendar.monthrange(year, month)
    if date > month_range[1]:
        month += 1
        if month >12:
            year += 1
            month -= 12
        date -= month_range[1]
    elif date<=0:
        month -= 1
        if month <=0:
            year -= 1
            month += 12
        date += month_range[1]
    for i in range(2):
        if len(str(time[i]))==1:
            time[i] = '0' + str(time[i])
        else:
            time[i] = str(time[i])
    time_res = ':'.join(time)
    return str(year)+'-'+str(month)+'-'+str(date)+' '+time_res

