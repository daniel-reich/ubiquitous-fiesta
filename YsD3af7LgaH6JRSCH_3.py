
def time_adjust(now, hrs, mins, sec):
    then=[0,0,0]
    secs=(hrs+int(now[:2]))*3600+(mins+int(now[3:5]))*60+sec+int(now[6:])
    then[0]=secs//3600%24
    then[1]=secs%3600//60
    then[2]=secs%60
    return ':'.join([str(i) if len(str(i))==2 else '0'+str(i) for i in then])

