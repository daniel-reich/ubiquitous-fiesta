
def bed_time(*times):
    lst = []
    for i in range(len(times)) :
        hrs = (24+int(times[i][0].split(':')[0])-int(times[i][1].split(':')[0])+(-1 if int(times[i][0].split(':')[1])<int(times[i][1].split(':')[1]) else 0))%24
        hrs = '0'*(2-len(str(hrs))) + str(hrs)
        min = (60+int(times[i][0].split(':')[1])-int(times[i][1].split(':')[1]))%60
        min = '0'*(2-len(str(min))) + str(min)
        lst.append(hrs+':'+min)
    return lst

