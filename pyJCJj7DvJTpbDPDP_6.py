
def days_between_dates(d1, d2):
    
    if (d1[4:] + d1[0:2] + d1[2:4]) > (d2[4:] + d2[0:2] + d2[2:4]):
        d1, d2 = d2, d1
​
    cnt_yrs = 0
    cnt_mths_d1 = 0 + int(d1[0:2])
    cnt_mths_d2 = 0 + int(d2[0:2])
​
    dict_norm = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30,
                 '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    dict_leap = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30,
                 '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
​
    for i in range(1, int(d1[2:4])):
        if d1[6:] == '00' and int(d1[4:]) % 400 == 0:
            cnt_mths_d1 += dict_leap[str(i)]
        elif d1[6:] != '00' and int(d1[4:]) % 4 == 0:
            cnt_mths_d1 += dict_leap[str(i)]
        else:
            cnt_mths_d1 += dict_norm[str(i)]
​
    for i in range(1, int(d2[2:4])):
        if d2[6:] == '00' and int(d2[4:]) % 400 == 0:
            cnt_mths_d2 += dict_leap[str(i)]
        elif d2[6:] != '00' and int(d2[4:]) % 4 == 0:
            cnt_mths_d2 += dict_leap[str(i)]
        else:
            cnt_mths_d2 += dict_norm[str(i)]
​
    for i in range(min(int(d1[4:]),int(d2[4:])), max(int(d1[4:]),int(d2[4:]))):
        if str(i)[len(str(i))-2:] == '00' and i % 400 == 0:
            cnt_yrs += 366
        elif str(i)[len(str(i))-2:] != '00' and i % 4 == 0:
            cnt_yrs += 366
        else:
            cnt_yrs += 365
​
    return cnt_yrs - cnt_mths_d1 + cnt_mths_d2

