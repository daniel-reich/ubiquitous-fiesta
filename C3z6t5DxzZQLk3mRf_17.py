
def tune(lst):
    return [comp(corr[i],lst[i]) for i in range(6)]
    
def comp(f1,f2):
    err = 100*(f2-f1)/f1
    if f2==0: return " - "
    if err<-2.5: return ">>+"
    if err<-0.5: return ">+"
    if err<0.5: return "OK"
    if err<2.5: return "+<"
    return "+<<"
​
corr = [329.63,246.94,196.00,146.83,110,82.41]

