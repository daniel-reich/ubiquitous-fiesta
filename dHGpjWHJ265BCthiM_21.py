
def current_streak(today, lst):
    today=today.split('-')
    today1=int(today[2])
    lst1=[]
    x=0
    for i in range(len(lst)):
        lst1=lst[len(lst)-1-i]['date'].split('-')
        lst1[2]=int(lst1[2])
        if today1==lst1[2]:
            today1-=1
            x+=1
        else: return x
    return x

