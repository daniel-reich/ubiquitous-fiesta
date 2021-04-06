
def track_robot (*steps):
    x=y=xs=ys=0
    for s in range(len(steps)):
        if s%2==0:
            if ys%2==0:
                y+=steps[s]
            else:
                y-=steps[s]
            ys+=1
        else:
            if xs%2==0:
                x+=steps[s]
            else:
                x-=steps[s]
            xs+=1
    return [x,y]

