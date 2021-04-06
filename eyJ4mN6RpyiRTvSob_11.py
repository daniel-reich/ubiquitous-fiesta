
def is_palindrome_possible(txt):
    revtxt = txt[::-1]
    if(txt == revtxt):
        return True
    else:
        lis = {}
        for i in txt:
            if(i in lis):
                lis[i] += 1
            else:
                lis[i] = 1
​
        l = []
        for i in lis.values():
            if(i % 2 != 0):
                l.append(1)
​
        if(len(l)  == 1):
            return True
        elif(len(l) == 0):
            return True
        else:
            return False

