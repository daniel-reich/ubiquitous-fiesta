
def microwave_buttons(time):
    i= ','.join(i for i in time).split(',')
    if int(i[3])>0 and i[3]=='3':return 2
    if int(i[3])>0 and i[3]!='3' or int(i[1])>0 and i[3]!='3':return 3
    if int(i[0])==0 and i[1]=='0':return 1
    return 5

