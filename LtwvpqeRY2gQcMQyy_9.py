
def sig_figs(num):
    count = 0
    leading_z = True
    last_index = 0
    for i in range(len(num)):
        if num[i].isdigit() is True:
            if int(num[i]) != 0:
                last_index = i
    for i in range(len(num)):
        if num[i].isdigit():
            if int(num[i]) != 0:
                count += 1
                leading_z = False
            else:
                if leading_z is False and i < last_index:
                    count += 1
                elif leading_z is False and i > last_index and "." in num:
                    count += 1
    return count

