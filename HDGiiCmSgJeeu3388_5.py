
def choose_fuse(fuses, current):
    current = "".join(list(current)[:-1])
    if "." in current:
        current = float(current)
    else:
        current = int(current)
​
    number = []
    for i in range(150):
        number.append(i)
    number = [str(i) for i in number]
​
    arr = []
    for i in fuses:
        arr.append(i.split("V"))
​
    arr2 = []
    for i in arr:
        for x in i:
            if x in number and x != "":
                arr2.append(x)
​
    arr2 = [int(i) for i in arr2]
    arr2.append(current)
    s = sorted(arr2)
​
    arr3 = s
    arr3 = [str(i) for i in arr3]
    for i in range(len(arr3)):
        arr3.append(arr3[i] + "V")
​
    answer = arr3[-3:]
​
    return answer[s.index(current)]

