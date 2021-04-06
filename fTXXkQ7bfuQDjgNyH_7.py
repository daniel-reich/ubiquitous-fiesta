
def day_of_year(date):
    days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    d= list(map(int,date.split("/")))
    if d[2] % 400 == 0:
         days[2]+=1
    elif d[2]%4 == 0 and d[2]%100!=0:
         days[2]+=1
    for i in range(1,len(days)):
         days[i]+=days[i-1]         
    return days[d[0]-1]+d[1]

