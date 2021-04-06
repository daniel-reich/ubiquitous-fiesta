
def diving_minigame(lst):
    diving_meter=10
    for i in lst:
​
        if i<0:
            diving_meter-=2
        elif i>0:
            if diving_meter!=10:
                diving_meter+=4
        if diving_meter==0:
            return False
    return True

