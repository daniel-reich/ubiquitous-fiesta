
def straight_digital(n):
    
    if n < 100:
        return "Not Straight"
    elif len(set(str(n))) == 1:
        return "Trivial Straight"
    else:
        r = int(str(n)[1]) - int(str(n)[0])
​
        for i in range(len(str(n))-1):
            if int(str(n)[i+1]) - int(str(n)[i]) != r:
                return "Not Straight"
​
        return r

