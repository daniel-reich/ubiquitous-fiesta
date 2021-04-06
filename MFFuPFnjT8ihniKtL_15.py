
def bug_jump(height, time):
    time/=1000
    tmax=height**.5    
    if time<tmax:
        hresult=height - (tmax-time)** 2
    else:
        hresult=max(0,height -(time-tmax)**2)    
    dirresult=None
    if time<=tmax :
        dirresult="up"
    elif tmax<time<=2*tmax:
        dirresult="down"    
    return [round(hresult,2),dirresult]

