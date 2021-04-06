
def kaprekar(num):
    if num == 6174:
            return 0
​
    for n in range(7):
        lst1 = list(sorted(str(num)))   #1-10
        lst2 = lst1[::-1]               #10-1
​
        if lst1[0] == "0":
            lst1.remove("0")
        
        if len(lst2) < 4:
            for i in range(4-len(lst2)):
                lst2.append("0")
​
        x, y = "", ""
        x1, y1 = 0, 0
        for i in lst1:
            x += i
        x1 = int(x)
    
        for i in lst2:
            y += i
        y1 = int(y)
​
        num = y1 - x1
​
        if num == 6174:
            return n + 1

