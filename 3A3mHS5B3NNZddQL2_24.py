
def interview(lst, tot):
    if len(lst) < 8 or tot > 120:
        return 'disqualified'
    elif (lst[0]+lst[1] > 10) or (lst[2]+lst[3] > 20) or (lst[4]+lst[5] > 30) or (lst[6]+lst[7] > 40):
        return 'disqualified'
    else:
        return 'qualified'

