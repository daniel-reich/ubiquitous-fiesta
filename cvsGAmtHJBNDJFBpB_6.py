
def can_traverse(list0):
    steps=len(list0[0])
    height=len(list0)
    result=True
    step_height0=0
    step_height1=0
    for i in range(steps):
        for j in range(height):
            step_height1+=list0[j][i]
        if step_height1<=step_height0+1 and step_height1 >=step_height0-1:
            step_height0=step_height1
            step_height1=0
            continue
        else:
            result=False
            break
    return result

