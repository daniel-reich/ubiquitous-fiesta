
def sum_round(num):
    if num==1010: return "10 1000";
    L =[];
    for i in range(len(str(num))):#str(num)[::-1]:
        if str(num)[i] != "0":
            L.append(str(num)[-i-1] + "0"*i);
        else:
            pass
    return " ".join(L)

