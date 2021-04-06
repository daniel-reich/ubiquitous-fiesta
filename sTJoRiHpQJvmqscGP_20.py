
def daily_streak(lst):
    v1=0
    v2=0
    for item in lst:
        if item:
            v2+=1
        else:
            if(v1<v2):
                v1=v2
            v2=0
        if(v1<v2):
            v1=v2
    return v1

