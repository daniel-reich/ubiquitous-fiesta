
def sig_figs(num):
    if float(num) == 0:
        return 0
    if len(str(num)) == 1:
        return 1
    cnt = 0
    if str(num)[0] == "-":
        str_num = str(num[1:])
    else:
        str_num = str(num)
    if "." not in str_num:
        if str_num[0] != "0":
            cnt += 1
        if str_num[-1] != "0":
            cnt += 1
        for i in range(1, len(str_num)-1):
            if str_num[i] != "0":
                cnt += 1
            elif str_num[i] == "0" and any(str_num[j] != "0" for j in range(0, i)) and any(str_num[j] != "0" for j in range(i + 1, len(str_num)-1)):
                cnt += 1
                print(str_num[i])
    elif "." in str_num:
        if str_num[0] != "0" and str_num[0] != ".":
            cnt += 1
        for i in range(1, len(str_num)-1):
            if str_num[i] != "0" and str_num[i] != ".":
                cnt += 1
            elif str_num[i] == "0" and not all(str_num[j] == "." or str_num[j] == "0" for j in range(0, i)) and \
                 any(str_num[j].isdigit() and str_num[j] != "0" for j in range(i+1, len(str_num)-1)):
                cnt += 1
            elif str_num[i] == "0" and all(str_num[j] == "0" for j in range(i+1, len(str_num)) if str_num[j] != "."):
                print(str_num[i])
                cnt += 1
        if str_num[-1] != ".":
           cnt += 1
    return cnt

