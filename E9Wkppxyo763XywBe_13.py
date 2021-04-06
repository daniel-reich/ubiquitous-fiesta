
def binary_clock(time):
    lst = [bin(int(each)).replace("0b","").rjust(2,"0").rjust(4," ") if idx == 0  else bin(int(each)).replace("0b","").rjust(3,"0").rjust(4, " ") if idx == 2 or idx == 4 else bin(int(each)).replace("0b","").rjust(4,"0") for idx, each in enumerate(time.replace(":",""))]
    newlst, newlst1 = [], []
    print(lst)
    leng = 0
    for i in range(4):
        for item in lst:
            newlst.append(item[leng])
        leng += 1
        newlst1.append(''.join(newlst))
        newlst = []
​
    return newlst1

