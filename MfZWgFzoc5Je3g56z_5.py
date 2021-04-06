
def translate(ran, num):
    lst_ran = [i for i in range(0, ran**2+1)]
    if num not in lst_ran:
        return str(num) + ' is not in the range ' + '[' + str(lst_ran[0]) + ':' + str(lst_ran[-1]) + ']'
    mir_num = lst_ran[-1] - num
​
    if num > mir_num:
        ct_up = lst_ran[-1] - num + mir_num + 1
        ct_dw = num - mir_num
        if ct_up == ct_dw:
            return format(ct_up, '+') + ' or '+ str(-ct_dw) + ' ---> ' + str(mir_num)
        else:
            return (format(ct_up, '+') if ct_up < ct_dw else str(-ct_dw)) + ' ---> ' + str(mir_num)
    else:
        ct_up = mir_num - num
        ct_dw = lst_ran[-1] - mir_num + num + 1
        if ct_up == ct_dw:
            return format(ct_up, '+') + ' or '+ str(-ct_dw) + ' ---> ' + str(mir_num)
        else:
            return (format(ct_up, '+') if ct_up < ct_dw else str(-ct_dw)) + ' ---> ' + str(mir_num)

